from typing import TYPE_CHECKING

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas import OrganizationDB
from src.utils.custom_types import AsyncFunc
from tests.fixtures import FakeBaseService, testing_cases
from tests.utils import BaseTestCase, compare_dicts_and_db_models

if TYPE_CHECKING:
    from collections.abc import Sequence

    from src.models import OrganizationModel


class TestBaseService:
    class _BaseService(FakeBaseService):
        _repo = 'organization'

    def __get_service(self, session: AsyncSession) -> FakeBaseService:
        return self._BaseService(session)

    @pytest.mark.usefixtures('setup_buildings')
    async def test_add_one(
            self,
            transaction_session: AsyncSession,
            first_organization: dict,
            get_organizations: AsyncFunc,
    ) -> None:
        service = self.__get_service(transaction_session)
        await service.add_one(**first_organization)

        users_in_db: Sequence[OrganizationModel] = await get_organizations()
        assert compare_dicts_and_db_models(users_in_db, [first_organization], OrganizationDB)

    @pytest.mark.usefixtures('setup_buildings')
    async def test_add_one_and_get_id(
            self,
            transaction_session: AsyncSession,
            first_organization: dict,
            get_organizations: AsyncFunc,
    ) -> None:
        service = self.__get_service(transaction_session)
        user_id = await service.add_one_and_get_id(**first_organization)
        assert user_id == first_organization.get('id')

        users_in_db: Sequence[OrganizationModel] = await get_organizations()
        assert compare_dicts_and_db_models(users_in_db, [first_organization], OrganizationDB)

    @pytest.mark.usefixtures('setup_buildings')
    async def test_add_one_and_get_obj(
            self,
            transaction_session: AsyncSession,
            first_organization: dict,
            get_organizations: AsyncFunc,
    ) -> None:
        service = self.__get_service(transaction_session)
        user = await service.add_one_and_get_obj(**first_organization)
        assert user.id == first_organization.get('id')

        users_in_db: Sequence[OrganizationModel] = await get_organizations()
        assert compare_dicts_and_db_models(users_in_db, [first_organization], OrganizationDB)

    @pytest.mark.usefixtures('setup_organizations')
    @pytest.mark.parametrize('case', testing_cases.TEST_BASE_SERVICE_GET_BY_QUERY_ONE_OR_NONE_PARAMS)
    async def test_get_by_filter_one_or_none(
            self,
            case: BaseTestCase,
            transaction_session: AsyncSession,
    ) -> None:
        service = self.__get_service(transaction_session)
        with case.expected_error:
            user_in_db: OrganizationModel | None = await service.get_by_filter_one_or_none(**case.data)
            result = None if not user_in_db else user_in_db.to_schema()
            assert result == case.expected_data

    @pytest.mark.usefixtures('setup_organizations')
    @pytest.mark.parametrize('case', testing_cases.TEST_BASE_SERVICE_GET_BY_QUERY_ALL_PARAMS)
    async def test_get_by_filter_all(
            self,
            case: BaseTestCase,
            transaction_session: AsyncSession,
    ) -> None:
        service = self.__get_service(transaction_session)
        with case.expected_error:
            users_in_db: Sequence[OrganizationModel] = await service.get_by_filter_all(**case.data)
            assert compare_dicts_and_db_models(users_in_db, case.expected_data, OrganizationDB)

    @pytest.mark.usefixtures('setup_organizations')
    @pytest.mark.parametrize('case', testing_cases.TEST_BASE_SERVICE_UPDATE_ONE_BY_ID_PARAMS)
    async def test_update_one_by_id(
            self,
            case: BaseTestCase,
            transaction_session: AsyncSession,
    ) -> None:
        service = self.__get_service(transaction_session)
        with case.expected_error:
            updated_user: OrganizationModel | None = await service.update_one_by_id(case.data.pop('_id'), **case.data)
            assert updated_user.to_schema() == case.expected_data

    @pytest.mark.usefixtures('setup_organizations')
    @pytest.mark.parametrize('case', testing_cases.TEST_BASE_SERVICE_DELETE_BY_QUERY_PARAMS)
    async def test_delete_by_filter(
            self,
            case: BaseTestCase,
            transaction_session: AsyncSession,
            get_organizations: AsyncFunc,
    ) -> None:
        service = self.__get_service(transaction_session)
        with case.expected_error:
            await service.delete_by_filter(**case.data)
            users_in_db: Sequence[OrganizationModel] = await get_organizations()
            assert compare_dicts_and_db_models(users_in_db, case.expected_data, OrganizationDB)

    @pytest.mark.usefixtures('setup_organizations')
    async def test_delete_all(
            self,
            transaction_session: AsyncSession,
            get_organizations: AsyncFunc,
    ) -> None:
        service = self.__get_service(transaction_session)
        await service.delete_all()
        users_in_db: Sequence[OrganizationModel] = await get_organizations()
        assert users_in_db == []
