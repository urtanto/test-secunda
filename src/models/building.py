from typing import TYPE_CHECKING

from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import BaseModel
from src.schemas.company import CompanyDB
from src.utils.custom_types import created_at, uuid_pk

if TYPE_CHECKING:
    from src.models import OrganizationModel


class BuildingModel(BaseModel):
    __tablename__ = 'building'

    id: Mapped[uuid_pk]
    address: Mapped[int] = mapped_column(String(255), nullable=False, unique=True)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)

    created_at: Mapped[created_at]

    organizations: Mapped[list["OrganizationModel"]] = relationship("OrganizationModel", back_populates="building")

    def to_schema(self) -> CompanyDB:
        return CompanyDB(**self.__dict__)
