from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.crud import get_user_by_username
from api.auth.schemas import RowSessionUser, TokenPayload
from api.auth.utils import decode_jwt

from api.core.db_helper import db_helper


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")


async def get_session_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    token: Annotated[str, Depends(oauth2_scheme)]
) -> RowSessionUser:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload: TokenPayload = decode_jwt(token)
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user: RowSessionUser = get_user_by_username(session, username)
    if user is None:
        raise credentials_exception
    return user