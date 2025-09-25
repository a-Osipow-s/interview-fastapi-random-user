from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends

from api.core.db_helper import db_helper


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/list")
async def get_list_of_books(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Get list of books."""
    ...


@router.get("/{book_id}/book")
async def get_book(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Get book."""
    ...


@router.post("/{book_id}/create")
async def create_book(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Create book."""
    ...


@router.put("/{book_id}/update")
async def update_book(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Update book."""
    ...


@router.delete("/{book_id}/delete")
async def delete_book(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    """Delete book."""
    ...

