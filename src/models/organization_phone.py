import uuid

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import Mapped

from src.models import BaseModel
from src.schemas.company import CompanyDB
from src.utils.custom_types import uuid_pk


class OrganizationPhoneModel(BaseModel):
    __tablename__ = 'organization_phone'

    id: Mapped[uuid_pk]
    organization_id: Mapped[uuid.UUID] = Column(ForeignKey("organization.id", ondelete="CASCADE", onupdate="CASCADE"))
    number: Mapped[str]

    def to_schema(self) -> CompanyDB:
        return CompanyDB(**self.__dict__)
