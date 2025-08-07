"""The module contains base routes for working with organization."""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from src.api.v1.services import OrganizationService
from src.schemas import BaseErrorResponse, OrganizationDB, OrganizationFilter, OrganizationResponse
from src.utils.auth import require_api_key

router = APIRouter(prefix='/organizations')


@router.post(
    path='/',
    description='Search an organization with filters.'
                '\n\nFields:'
                '\n- "path": category'
                '\n- "id": building id'
                '\n- "address": address of a building'
                '\n- "latitude": coordinate of a point for geo filtering'
                '\n- "longitude": coordinate of a point for geo filtering'
                '\n- "type": type of geo filtering'
                '\n- "radius": radius in km for radius geo filtering'
                '\n- "width": width of rectangle in km for geo filtering'
                '\n- "height": height of rectangle in km for geo filtering'
                '\n- "name": name or part of name of organization',
    dependencies=[Depends(require_api_key)],
    status_code=HTTP_200_OK,
    responses={
        HTTP_200_OK: {
            'model': OrganizationResponse,
            'description': 'Organizations got successfully.',
        },
        HTTP_400_BAD_REQUEST: {
            'model': BaseErrorResponse,
            'description': 'Invalid data',
        },
    },
)
async def search_organizations(
        filters: OrganizationFilter,
        service: OrganizationService = Depends(),
) -> OrganizationResponse | BaseErrorResponse:
    try:
        organizations: list[OrganizationDB] = await service.search(filters)
    except ValueError as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))
    return OrganizationResponse(payload=organizations)


@router.get(
    path='/{org_id}',
    description='Get an organization by id.',
    status_code=HTTP_200_OK,
    dependencies=[Depends(require_api_key)],
    responses={
        HTTP_200_OK: {
            'model': OrganizationResponse,
            'description': 'Organization got successfully.',
        },
        HTTP_400_BAD_REQUEST: {
            'model': BaseErrorResponse,
            'description': 'Invalid data',
        },
    },
)
async def get_organization(
        org_id: UUID4,
        service: OrganizationService = Depends(),
) -> OrganizationResponse:
    """Get organizations by ID.

    :param org_id: ID of the organization
    :param service: Organization service

    Returns
    -------
    BaseResponse with organization

    """
    try:
        organization: OrganizationDB | None = await service.get_company_by_id(org_id)
    except ValueError as e:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=str(e))
    return OrganizationResponse(payload=organization)
