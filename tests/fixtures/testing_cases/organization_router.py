import os
import uuid

from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_422_UNPROCESSABLE_ENTITY

from tests.constants import BASE_ENDPOINT_URL
from tests.fixtures.db_mocks import BUILDINGS, ORGANIZATIONS
from tests.utils import RequestTestCase, json_serializable

TEST_ORGANIZATION_ROUTE_FILTER_PARAMS: list[RequestTestCase] = [
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={},
        expected_status=HTTP_200_OK,
        expected_data=json_serializable(ORGANIZATIONS),
        description='Just request',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'latitude': 'test',
        },
        expected_status=HTTP_422_UNPROCESSABLE_ENTITY,
        expected_data={},
        description='Not valid request body',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'id': str(ORGANIZATIONS[0]['building_id']),
        },
        expected_status=HTTP_200_OK,
        expected_data=json_serializable([ORGANIZATIONS[0]]),
        description='building_id filter',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'address': BUILDINGS[1]['address'],
        },
        expected_status=HTTP_200_OK,
        expected_data=json_serializable([ORGANIZATIONS[1], ORGANIZATIONS[5]]),
        description='address filter',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'name': 'ООО',
        },
        expected_status=HTTP_200_OK,
        expected_data=json_serializable([ORGANIZATIONS[0], ORGANIZATIONS[2], *ORGANIZATIONS[5:]]),
        description='name filter',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'type': 'ООО',
        },
        expected_status=HTTP_422_UNPROCESSABLE_ENTITY,
        expected_data={},
        description='circle filter bad type',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'type': 'RADIUS',
            'latitude': 55.7539,
            'longitude': 37.6208,
        },
        expected_status=HTTP_422_UNPROCESSABLE_ENTITY,
        expected_data={},
        description='circle filter no radius',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'type': 'RADIUS',
            'latitude': 55.7539,
            'longitude': 37.6208,
            'radius': 'd',
        },
        expected_status=HTTP_422_UNPROCESSABLE_ENTITY,
        expected_data={},
        description='circle filter bad radius',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'type': 'RADIUS',
            'latitude': 55.7539,
            'longitude': 37.6208,
            'radius': 2,
        },
        expected_status=HTTP_200_OK,
        expected_data=json_serializable(
            [*ORGANIZATIONS[: 3], *ORGANIZATIONS[5: 7]],
        ),
        description='circle filter',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'type': 'RECTANGLE',
            'latitude': 55.7539,
            'longitude': 37.6208,
            'radius': 2,
        },
        expected_status=HTTP_422_UNPROCESSABLE_ENTITY,
        expected_data={},
        description='rectangle filter bad params',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'type': 'RECTANGLE',
            'latitude': 55.7539,
            'longitude': 37.6208,
            'width': 6,
            'heigh': '6',
        },
        expected_status=HTTP_422_UNPROCESSABLE_ENTITY,
        expected_data={},
        description='rectangle filter bad params',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        data={
            'type': 'RECTANGLE',
            'latitude': 55.7539,
            'longitude': 37.6208,
            'width': 2,
            'height': 2,
        },
        expected_status=HTTP_200_OK,
        expected_data=json_serializable(
            [*ORGANIZATIONS[: 2], ORGANIZATIONS[5]],
        ),
        description='rectangle filter',
    ),
]

TEST_ORGANIZATIONS_ROUTE_GET_PARAMS: list[RequestTestCase] = [
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/{ORGANIZATIONS[1]["id"]}',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        expected_status=HTTP_200_OK,
        expected_data=json_serializable(ORGANIZATIONS[1]),
        description='Positive case',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/{uuid.uuid4()}',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        expected_status=HTTP_400_BAD_REQUEST,
        expected_data={},
        description='Negative case',
    ),
    RequestTestCase(
        url=f'{BASE_ENDPOINT_URL}/organizations/ddddd',
        headers={'X-API-KEY': os.getenv('API_KEY')},
        expected_status=HTTP_422_UNPROCESSABLE_ENTITY,
        expected_data={},
        description='Unvalid case',
    ),
]
