import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import BaseModel
from src.utils.custom_types import created_at, uuid_pk

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import BuildingModel
    from src.models import OrganizationPhoneModel
    from src.models import ActivityModel


class OrganizationModel(BaseModel):
    __tablename__ = "organization"

    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    building_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("building.id"), nullable=False)
    created_at: Mapped[created_at]

    building: Mapped["BuildingModel"] = relationship(back_populates="organizations")
    phones: Mapped[list["OrganizationPhoneModel"]] = relationship(
        back_populates=None,
        cascade="all, delete-orphan"
    )
    activities: Mapped[list["ActivityModel"]] = relationship(
        secondary="organization_activity",
        back_populates="organizations"
    )
