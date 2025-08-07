from pydantic import UUID4, BaseModel, Field


class OrganizationPhoneDB(BaseModel):
    id: UUID4 = Field(..., description='Unique identifier of the phone')
    organization_id: UUID4 = Field(..., description='Unique identifier of the organization')
    number: str = Field(..., description='Phone number of the organization')
