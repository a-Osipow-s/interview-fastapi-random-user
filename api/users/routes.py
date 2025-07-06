from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, Response, status

from api.core.db_helper import db_helper
from api.users import crud
from api.users.schemas import UserCreate
from api.utils.password import hash_password

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user_create: UserCreate
):
    user_create.password = hash_password(user_create.password).decode()
    await crud.create_user(session, user_create)
    return Response("User created", status_code=status.HTTP_201_CREATED)