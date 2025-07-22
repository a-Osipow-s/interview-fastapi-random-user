from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException, status

from api.auth.schemas import RowSessionUser
from api.users.crud import get_user_core_by_username
from api.models import UserCore


_invalid_email_password_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid email or password",
    headers={"WWW-Authenticate": "Bearer"},
)         


async def authorize_user(
    session: AsyncSession,
    username: str,
    password: str,
) -> UserCore:
    user: UserCore = await get_user_core_by_username(
        session, username
    )
    if not user:
        raise _invalid_email_password_exception
    
    if not user.validate_password(password):
        raise _invalid_email_password_exception
    
    return user


async def get_session_user_by_username(
    session: AsyncSession, 
    username: str
) -> RowSessionUser:
    stmt = select(
        UserCore.id, UserCore.username, UserCore.email
    ).where(
        UserCore.username == username
    )
    result: Result = await session.execute(stmt)
    return result.one_or_none()
