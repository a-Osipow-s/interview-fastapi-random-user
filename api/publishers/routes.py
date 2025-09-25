from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends

from api.core.db_helper import db_helper


router = APIRouter(prefix="/publishers", tags=["Publishers"])


@router.get("/list")
async def get_list_of_publishers(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Get list of publishers."""
    ...


@router.get("/{publisher_id}/publisher")
async def get_publisher(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Get publisher."""
    ...


@router.post("/{publisher_id}/create")
async def create_publisher(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Create publisher."""
    ...


@router.put("/{publisher_id}/update")
async def update_publisher(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Update publisher."""
    ...


@router.delete("/{publisher_id}/delete")
async def delete_publisher(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Delete publisher."""
    ...
