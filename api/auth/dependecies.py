from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.crud import get_session_user_by_username
from api.auth.schemas import RowSessionUser, TokenPayload
from api.auth.utils import decode_jwt

from api.core.db_helper import db_helper


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/sessions/")

_credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def _get_token_paylaod(token: str) -> TokenPayload:
    try:
        payload: TokenPayload = decode_jwt(token)
    except InvalidTokenError:
        raise _credentials_exception

    return payload

async def _get_user_data_by_token_payload(
    session: AsyncSession,
    payload: TokenPayload,
) -> RowSessionUser:
    username: str = payload.get('sub')
    if not username:
        raise _credentials_exception

    return await get_session_user_by_username(session, username)

async def get_session_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    token: Annotated[str, Depends(oauth2_scheme)]
) -> RowSessionUser:    
    payload: TokenPayload = _get_token_paylaod(token)
    user: RowSessionUser = _get_user_data_by_token_payload(session, payload)

    if not user:
        raise _credentials_exception

    return user