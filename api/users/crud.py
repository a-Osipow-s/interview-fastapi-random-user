from sqlalchemy.ext.asyncio import AsyncSession


from api.models import UserCore
from api.users.schemas import UserCreate


async def create_user(session: AsyncSession, user_create: UserCreate) -> None:
    session.add(UserCore(**user_create.model_dump()))
    await session.commit()
