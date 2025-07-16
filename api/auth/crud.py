from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.schemas import RowSessionUser
from api.models.users import UserCore


async def get_user_core_by_username(
    session: AsyncSession,
    username: str,
) -> UserCore:
    stmt = select(
        UserCore
    ).where(
        UserCore.username == username
    )
    result: Result = await session.scalars(stmt)
    return result.one_or_none()


async def get_session_user_by_username(
    session: AsyncSession, 
    username: str
) -> RowSessionUser:
    stmt = select(
        UserCore.id, UserCore.username, UserCore.email
    ).where(
        UserCore.username == username
    )
    result: Result = await session.scalars(stmt)
    return result.one_or_none()
