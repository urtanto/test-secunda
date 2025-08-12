"""The package contains basic data for tests for the postgres database."""

from tests.fixtures.db_mocks.activities import ACTIVITIES
from tests.fixtures.db_mocks.buildings import BUILDINGS
from tests.fixtures.db_mocks.organization_activities import ORGANIZATION_ACTIVITIES
from tests.fixtures.db_mocks.organization_phones import ORGANIZATION_PHONES
from tests.fixtures.db_mocks.organizations import ORGANIZATIONS

__all__ = (
    'ACTIVITIES',
    'BUILDINGS',
    'ORGANIZATIONS',
    'ORGANIZATION_ACTIVITIES',
    'ORGANIZATION_PHONES',
)
