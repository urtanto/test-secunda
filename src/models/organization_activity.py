import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models import BaseModel


class OrganizationActivityModel(BaseModel):
    __tablename__ = 'organization_activity'

    organization_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('organization.id'), primary_key=True)
    activity_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('activity.id'), primary_key=True)
