from collections.abc import Sequence
from copy import deepcopy

import pytest
import pytest_asyncio
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import (
    ActivityModel,
    BuildingModel,
    OrganizationActivityModel,
    OrganizationModel,
    OrganizationPhoneModel,
)
from src.utils.custom_types import AsyncFunc
from tests import fixtures
from tests.utils import bulk_save_models


@pytest.fixture
def activities() -> tuple[dict]:
    return deepcopy(fixtures.db_mocks.ACTIVITIES)


@pytest.fixture
def buildings() -> tuple[dict]:
    return deepcopy(fixtures.db_mocks.BUILDINGS)


@pytest.fixture
def organizations() -> tuple[dict]:
    return deepcopy(fixtures.db_mocks.ORGANIZATIONS)


@pytest.fixture
def organizations_activities() -> tuple[dict]:
    return deepcopy(fixtures.db_mocks.ORGANIZATION_ACTIVITIES)


@pytest.fixture
def organizations_phones() -> tuple[dict]:
    return deepcopy(fixtures.db_mocks.ORGANIZATION_PHONES)


@pytest_asyncio.fixture
async def setup_activities(transaction_session: AsyncSession, activities: tuple[dict]) -> None:
    """Creates activities that will only exist within the session."""
    await bulk_save_models(transaction_session, ActivityModel, activities)


@pytest_asyncio.fixture
async def setup_buildings(transaction_session: AsyncSession, buildings: tuple[dict]) -> None:
    """Creates buildings that will only exist within the session."""
    await bulk_save_models(transaction_session, BuildingModel, buildings)


@pytest_asyncio.fixture
async def setup_organizations(
        transaction_session: AsyncSession,
        organizations: tuple[dict],
        setup_buildings: None
) -> None:
    """Creates organizations that will only exist within the session."""
    await bulk_save_models(transaction_session, OrganizationModel, organizations)


@pytest_asyncio.fixture
async def setup_organizations_phones(
        transaction_session: AsyncSession,
        organizations_phones: tuple[dict],
        setup_organizations: None
) -> None:
    """Creates organizations_phones that will only exist within the session."""
    await bulk_save_models(transaction_session, OrganizationPhoneModel, organizations_phones)


@pytest_asyncio.fixture
async def setup_organizations_activities(
        transaction_session: AsyncSession,
        organizations_activities: tuple[dict],
        setup_organizations: None,
        setup_activities: None
) -> None:
    """Creates organizations_activities that will only exist within the session."""
    await bulk_save_models(transaction_session, OrganizationActivityModel, organizations_activities)


@pytest.fixture
def first_organization() -> dict:
    return deepcopy(fixtures.db_mocks.ORGANIZATIONS[0])


@pytest_asyncio.fixture
def get_organizations(transaction_session: AsyncSession) -> AsyncFunc:
    """Get user.

    Returns
    -------
    users existing within the session

    """

    async def _get_users() -> Sequence[OrganizationModel]:
        res: Result = await transaction_session.execute(select(OrganizationModel))
        return res.scalars().all()

    return _get_users
