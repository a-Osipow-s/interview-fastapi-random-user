from sqlalchemy import select
from sqlalchemy.engine import Result, Row
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.schemas import SessionUser
from api.models.users import UserCore


async def get_user_by_username(
    session: AsyncSession, 
    username: str
) -> Row[SessionUser]:
    stmt = select(
        UserCore.id, UserCore.username, UserCore.email
    ).where(
        UserCore.username == username
    )
    result: Result = await session.execute(stmt)
    return result.one_or_none()