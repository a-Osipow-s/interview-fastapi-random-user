from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.schemas import RowSessionUser
from api.models import UserCore


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
