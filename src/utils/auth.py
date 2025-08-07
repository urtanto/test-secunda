from fastapi import Depends, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from src.config import Settings


def require_api_key(key: str | None = Depends(Settings.API_HEADER)):
    if key != Settings.API_KEY:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                            detail='Invalid or missing API key')
