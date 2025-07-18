from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, Form, HTTPException, status

from api.auth.crud import get_user_core_by_username
from api.auth.schemas import Token, LoginForm
from api.auth.utils import encode_jwt

from api.core.db_helper import db_helper

from api.models.users import UserCore

from api.utils.password import hash_password


router = APIRouter(prefix="/auth", tags=["AUTH"])


@router.post("/sessions/", response_model=Token)
async def login(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    login_form: Annotated[LoginForm, Form()],
):
    user: UserCore = await get_user_core_by_username(
        session, login_form.username
    )

    if not user or not user.validate_password(login_form.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )         

    jwt_payload: dict = {
        "sub": user.id,
        "username": user.username
    }
    access_token: str = encode_jwt(jwt_payload)
    return Token(
        access_token=access_token,
        token_type="Bearer"
    )


@router.delete("/sessions/")
async def logout():
    # revoked token, add to blacklist
    pass