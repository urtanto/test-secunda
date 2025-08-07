from pydantic import UUID4, BaseModel, Field, PastDatetime

from src.schemas.activity import ActivityFilter
from src.schemas.building import BuildingDB, BuildingFilter, GeoFilter
from src.schemas.response import BaseResponse


class OrganizationNameFilter(BaseModel):
    name: str | None = Field(None, description='Organization name')


class OrganizationFilter(OrganizationNameFilter, GeoFilter, BuildingFilter, ActivityFilter):
    pass


class OrganizationDB(BaseModel):
    id: UUID4 = Field(..., description='Unique ID of an organization')
    name: str = Field(..., description='Name of the organization')
    building_id: UUID4 = Field(..., description='Unique ID of an building')
    created_at: PastDatetime = Field(..., description='Datetime of creating building')

    buildings: BuildingDB | None = Field(None, description='Buildings associated with this organization')
    phones: list[str] | None = Field(None, description='Phones associated with this organization')
    activities: list[str] | None = Field(None, description='Activity associated with this organization')


class OrganizationResponse(BaseResponse):
    payload: OrganizationDB | list[OrganizationDB] | None = Field(None)
