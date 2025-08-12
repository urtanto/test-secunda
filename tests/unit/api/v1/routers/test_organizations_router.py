"""Contains tests for user routes."""

import pytest
from httpx import AsyncClient

from tests.fixtures import testing_cases
from tests.utils import RequestTestCase, prepare_payload


class TestOrganizationRouter:
    exclude: tuple[str] = ['activities', 'buildings', 'phones', 'created_at']

    @staticmethod
    @pytest.mark.usefixtures('setup_organizations_phones')
    @pytest.mark.usefixtures('setup_organizations_activities')
    @pytest.mark.parametrize('case', testing_cases.TEST_ORGANIZATION_ROUTE_FILTER_PARAMS)
    async def test_search(
        case: RequestTestCase,
        async_client: AsyncClient,
    ) -> None:
        with case.expected_error:
            response = await async_client.post(case.url, json=case.data, headers=case.headers)
            assert response.status_code == case.expected_status
            assert prepare_payload(
                response,
                exclude=TestOrganizationRouter.exclude,
            ) == prepare_payload(case.expected_data, exclude=TestOrganizationRouter.exclude)

    @staticmethod
    @pytest.mark.usefixtures('setup_organizations')
    @pytest.mark.parametrize('case', testing_cases.TEST_ORGANIZATIONS_ROUTE_GET_PARAMS)
    async def test_get(
        case: RequestTestCase,
        async_client: AsyncClient,
    ) -> None:
        with case.expected_error:
            response = await async_client.get(case.url, headers=case.headers)
            assert response.status_code == case.expected_status
            assert prepare_payload(
                response,
                exclude=TestOrganizationRouter.exclude,
            ) == prepare_payload(case.expected_data, exclude=TestOrganizationRouter.exclude)
