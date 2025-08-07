from pydantic import UUID4, BaseModel, Field


class ActivityFilter(BaseModel):
    path: str | None = Field(None, description='Type of activity')


class ActivityDB(BaseModel):
    id: UUID4 = Field(..., description='Unique identifier of the task')
    path: str = Field(..., description='Type of activity')
    name: str = Field(..., description='Name of the activity')
