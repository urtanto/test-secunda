from typing import TYPE_CHECKING

from pydantic import UUID4

from src.schemas import OrganizationDB
from src.schemas.organization import OrganizationFilter
from src.utils.service import BaseService, transaction_mode

if TYPE_CHECKING:
    from src.models import OrganizationModel


class OrganizationService(BaseService):
    _repo: str = 'organization'

    @transaction_mode
    async def search(self, filters: OrganizationFilter) -> list[OrganizationDB]:
        organizations: list[OrganizationModel] = await self.uow.organization.search(filters)
        return [x.to_schema() for x in organizations]

    @transaction_mode
    async def get_company_by_id(self, org_id: UUID4) -> OrganizationDB:
        organization: OrganizationModel = await self.uow.organization.get_by_id(org_id)

        if organization is None:
            err_text = f'Organization {org_id} not found'
            raise ValueError(err_text)

        return organization.to_schema()
