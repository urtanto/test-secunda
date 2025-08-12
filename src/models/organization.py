import uuid
from typing import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, attributes, mapped_column, relationship

from src.models import BaseModel
from src.schemas import OrganizationDB
from src.utils.custom_types import created_at, uuid_pk

if TYPE_CHECKING:
    from src.models import ActivityModel, BuildingModel, OrganizationPhoneModel


class OrganizationModel(BaseModel):
    __tablename__ = 'organization'

    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(String(255), unique=False, nullable=False)
    building_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('building.id'), nullable=False)
    created_at: Mapped[created_at]

    building: Mapped['BuildingModel'] = relationship(back_populates='organizations')
    phones: Mapped[list['OrganizationPhoneModel']] = relationship(
        back_populates=None,
        cascade='all, delete-orphan',
    )
    activities: Mapped[list['ActivityModel']] = relationship(
        secondary='organization_activity',
        back_populates='organizations',
    )

    def to_schema(self) -> OrganizationDB:
        organization = OrganizationDB(
            id=self.id,
            name=self.name,
            building_id=self.building_id,
            created_at=self.created_at,
        )
        insp = sa.inspect(self)

        if insp.attrs.building.loaded_value is not attributes.NO_VALUE:
            organization.buildings = self.building.to_schema()
        if insp.attrs.phones.loaded_value is not attributes.NO_VALUE:
            organization.phones = [x.to_schema().number for x in self.phones]
        if insp.attrs.activities.loaded_value is not attributes.NO_VALUE:
            organization.activities = [x.to_schema().name for x in self.activities]

        return organization
