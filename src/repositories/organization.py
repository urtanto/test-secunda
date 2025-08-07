from math import cos, radians

from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy import Select, func, select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy_utils import Ltree

from src.models import ActivityModel, BuildingModel, OrganizationModel
from src.schemas import OrganizationFilter
from src.utils.enums import GeoType
from src.utils.repository import SqlAlchemyRepository


class OrganizationRepository(SqlAlchemyRepository[OrganizationModel]):
    _model = OrganizationModel

    async def get_by_id(self, org_id: UUID4) -> OrganizationModel:
        """Get organization by id.

        :param org_id: Organization id

        Returns
        -------
        BaseResponse with organization

        """
        query = select(self._model).filter(self._model.id == org_id)
        query = query.options(
            selectinload(self._model.activities),
            joinedload(self._model.building),
            joinedload(self._model.phones),
        )

        result = await self._session.execute(query)
        return result.unique().scalars().first()

    async def search(self, filters: OrganizationFilter) -> list[OrganizationModel]:
        """Searches for organizations matching the given filters.

        :param filters: filters to apply to the query

        Returns
        -------
        list of OrganizationModel.

        """
        query = select(self._model)
        joined_building = False

        query = await self._organization_filter(query, filters)
        query, joined_building = await self._building_filter(query, filters, joined_building)
        query, joined_building = await self._geotype_filter(query, filters, joined_building)
        query = await self._activity_filter(query, filters)

        query = query.options(
            selectinload(self._model.activities),
            selectinload(self._model.building),
            selectinload(self._model.phones),
        )

        result = await self._session.execute(query)
        return list(result.unique().scalars().all())

    async def _organization_filter(self, query: Select, filters: OrganizationFilter) -> Select:
        if filters.name:
            query = query.where(self._model.name.ilike(f'%{filters.name}%'))
        return query

    @staticmethod
    async def _building_filter(query: Select, filters: OrganizationFilter, joined_building: bool) -> type[Select, bool]:
        if filters.id or filters.address:
            query = query.join(OrganizationModel.building)
            joined_building = True

            if filters.id:
                query = query.where(BuildingModel.id == filters.id)

            if filters.address:
                query = query.where(BuildingModel.address.ilike(f'%{filters.address}%'))
        return query, joined_building

    @staticmethod
    async def _geotype_filter(query: Select, filters: OrganizationFilter, joined_building: bool) -> type[Select, bool]:
        if filters.latitude and filters.longitude:
            if not joined_building:
                query = query.join(OrganizationModel.building)

            lat0 = filters.latitude
            lon0 = filters.longitude

            if filters.type == GeoType.RADIUS:
                if filters.radius is None:
                    raise HTTPException(
                        status_code=400,
                        detail='Invalid radius value',
                    )

                r_km = filters.radius

                distance_expr = (
                        6371 * func.acos(
                    func.cos(func.radians(lat0))
                    * func.cos(func.radians(BuildingModel.latitude))
                    * func.cos(
                        func.radians(BuildingModel.longitude) - func.radians(lon0),
                    )
                    + func.sin(func.radians(lat0))
                    * func.sin(func.radians(BuildingModel.latitude)),
                )
                )

                query = query.where(distance_expr <= r_km)

            if filters.type == GeoType.RECTANGLE:
                if filters.width is None or filters.height is None:
                    raise HTTPException(
                        status_code=400,
                        detail='Invalid width or height value',
                    )

                half_h_deg = (filters.height / 2) / 111.045
                half_w_deg = (filters.width / 2) / (111.045 * cos(radians(lat0)))

                min_lat, max_lat = lat0 - half_h_deg, lat0 + half_h_deg
                min_lon, max_lon = lon0 - half_w_deg, lon0 + half_w_deg

                query = query.where(
                    BuildingModel.latitude.between(min_lat, max_lat),
                    BuildingModel.longitude.between(min_lon, max_lon),
                )
        return query, joined_building

    async def _activity_filter(self, query: Select, filters: OrganizationFilter) -> Select:
        if filters.path:
            org_type = (
                await self._session.execute(
                    select(ActivityModel).filter(ActivityModel.path == Ltree(filters.path)),
                )
            ).scalar_one_or_none()

            if org_type is None:
                raise HTTPException(status_code=400, detail=f'Activity path {filters.path} not found')

            query = query.filter(
                self._model.activities.any(
                    ActivityModel.path.descendant_of(org_type.path),
                ),
            )
        return query
