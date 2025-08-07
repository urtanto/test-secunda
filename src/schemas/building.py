from pydantic import UUID4, BaseModel, Field, PastDatetime, model_validator

from src.utils.constans import Exceptions
from src.utils.enums import GeoType


class BuildingFilter(BaseModel):
    id: UUID4 | None = Field(None, description='Unique identifier of the building')
    address: str | None = Field(None, description='Address of the building')


class GeoFilter(BaseModel):
    latitude: float | None = Field(None, description='Latitude of the point on the map')
    longitude: float | None = Field(None, description='Longitude of the point on the map')
    type: GeoType | None = Field(None, description='Type of the filtering')
    radius: float | None = Field(None, description='Radius of the circle filtering')
    width: float | None = Field(None, description='width of the rectangle filtering')
    height: float | None = Field(None, description='height of the rectangle filtering')

    @model_validator(mode='after')
    def validating(cls, m: 'GeoFilter'):
        if (m.latitude is None) ^ (m.longitude is None):
            raise ValueError(
                Exceptions.NOT_CORRECT_COORDS,
            )

        if m.latitude is not None and m.longitude is not None:
            if m.type is None:
                raise ValueError(
                    Exceptions.NO_TYPE_FILTERING,
                )

            if m.type == GeoType.RADIUS and m.radius is None:
                raise ValueError(
                    Exceptions.RADIUS_NOT_SELECTED,
                )

            if m.type == GeoType.RECTANGLE and (m.width is None or m.height is None):
                raise ValueError(
                    Exceptions.RECTANGLE_SIZES_NOT_DEFINED,
                )

        return m


class BuildingDB(BaseModel):
    id: UUID4 = Field(..., description='Unique identifier of the building')
    address: str = Field(..., description='Address of the building')
    latitude: float = Field(..., description='Latitude of the point on the map')
    longitude: float = Field(..., description='Longitude of the point on the map')
    created_at: PastDatetime = Field(..., description='Datetime of creating building')
