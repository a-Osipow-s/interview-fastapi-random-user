from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends

from api.core.db_helper import db_helper


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/list")
async def get_users(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Get random users."""
    ...


@router.get("/{user_id}/user")
async def get_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Get random user."""
    ...


@router.post("/{user_id}/create")
async def create_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Create new random user."""
    ...


@router.put("/{user_id}/update")
async def update_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Update random user."""
    ...


@router.delete("/{user_id}/delete")
async def delete_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Delete random user."""
    ...

