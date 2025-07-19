from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


from api.models import UserCore
from api.users.schemas import UserCreate


async def create_user(session: AsyncSession, user_create: UserCreate) -> None:
    session.add(UserCore(**user_create.model_dump()))
    await session.commit()


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