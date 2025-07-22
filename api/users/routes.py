from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, Form, Response, status

from api.core.db_helper import db_helper
from api.users import crud
from api.users.schemas import UserCreate


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user_create: Annotated[UserCreate, Form()]
):
    """Create new user. User sign up."""
    await crud.create_user(session, user_create)
    return Response("User created", status_code=status.HTTP_201_CREATED)