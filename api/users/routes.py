from typing import Annotated, List

# from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, HTTPException, status

from api.users.schemas import UserIn, UserOut
from api.users.crud import user_service
from api.models.user_mongo import PydanticObjectId

# from api.core.db_helper import db_helper


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/list", response_model=List[UserOut])
async def get_users():
    """Get all users."""
    return await user_service.list_users()


@router.get("/{user_id}/user", response_model=UserOut)
async def get_user(user_id: PydanticObjectId):
    """Get user by ID."""
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user



@router.post("/create", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserIn):
    """Create new user."""
    return await user_service.create_user(user_in)


@router.put("/{user_id}/update", response_model=UserOut)
async def update_user(user_id: PydanticObjectId, user_in: UserIn):
    """Update existing user."""
    user = await user_service.update_user(user_id, user_in)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.delete("/{user_id}/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: PydanticObjectId):
    """Delete user by ID."""
    deleted = await user_service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
