from uuid import uuid4

from src.schemas.organization import OrganizationDB
from tests.fixtures.db_mocks import ORGANIZATIONS
from tests.utils import BaseTestCase

TEST_BASE_SERVICE_GET_BY_QUERY_ONE_OR_NONE_PARAMS: list[BaseTestCase] = [
    BaseTestCase(
        data={'id': ORGANIZATIONS[0]['id']},
        expected_data=OrganizationDB(
            id=ORGANIZATIONS[0]['id'],
            name=ORGANIZATIONS[0]['name'],
            building_id=ORGANIZATIONS[0]['building_id'],
            created_at=ORGANIZATIONS[0]['created_at'],
        ),
    ),
    BaseTestCase(
        data={'id': uuid4()},
        expected_data=None,
    ),
]

TEST_BASE_SERVICE_GET_BY_QUERY_ALL_PARAMS: list[BaseTestCase] = [
    BaseTestCase(data={'id': ORGANIZATIONS[0]['id']}, expected_data=[ORGANIZATIONS[0]]),
    BaseTestCase(data={'id': uuid4()}, expected_data=[]),
]

TEST_BASE_SERVICE_UPDATE_ONE_BY_ID_PARAMS: list[BaseTestCase] = [
    BaseTestCase(
        data={
            '_id': ORGANIZATIONS[0]['id'],
            'name': 'test',
        },
        expected_data=OrganizationDB(
            id=ORGANIZATIONS[0]['id'],
            name='test',
            building_id=ORGANIZATIONS[0]['building_id'],
            created_at=ORGANIZATIONS[0]['created_at'],
        ),
    ),
]

TEST_BASE_SERVICE_DELETE_BY_QUERY_PARAMS: list[BaseTestCase] = [
    BaseTestCase(data={'id': ORGANIZATIONS[0]['id']}, expected_data=ORGANIZATIONS[1:]),
    BaseTestCase(data={'id': uuid4()}, expected_data=ORGANIZATIONS),
    BaseTestCase(data={}, expected_data=[]),
]
