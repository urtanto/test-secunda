from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import LtreeType

from src.models.base import BaseModel
from src.schemas import ActivityDB
from src.utils.custom_types import uuid_pk

if TYPE_CHECKING:
    from src.models import OrganizationModel


class ActivityModel(BaseModel):
    __tablename__ = 'activity'

    id: Mapped[uuid_pk]
    path: Mapped[str] = mapped_column(LtreeType, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)

    organizations: Mapped[list['OrganizationModel']] = relationship(
        secondary='organization_activity',
        back_populates='activities',
    )

    def to_schema(self) -> ActivityDB:
        return ActivityDB(
            id=self.id,
            path=str(self.path),
            name=self.name,
        )
