from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from api.auth.crud import get_user_by_username
from api.auth.schemas import RowSessionUser, Token
from api.auth.utils import encode_jwt

from api.core.db_helper import db_helper

router = APIRouter(prefix="/auth", tags=["AUTH"])


@router.post("/sessions/", response_model=Token)
async def login(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    # https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#update-the-dependencies
    user: RowSessionUser  = await get_user_by_username(
        session, 
        form_data.username
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