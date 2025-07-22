from typing import Annotated

from redis.asyncio.client import Redis as ClientRedis
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import ( 
    APIRouter, 
    Depends, 
    Form, 
    Response, 
    status
)

from api.auth.crud import authorize_user
from api.auth.dependecies import get_session_user, oauth2_scheme
from api.auth.schemas import Token, LoginForm, RowSessionUser
from api.auth.utils import encode_jwt

from api.core.db_helper import db_helper
from api.core.cache_helper import cache_helper

from api.models import UserCore


router = APIRouter(prefix="/auth", tags=["AUTH"])


@router.post("/sessions/", response_model=Token)
async def login(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    login_form: Annotated[LoginForm, Form()],
):
    user: UserCore = await authorize_user(
        session, login_form.username, login_form.password
    )

    jwt_payload: dict = {
        "sub": user.username,
        "id": user.id,
        "email": user.email,
    }
    access_token: str = encode_jwt(jwt_payload)
    return Token(
        access_token=access_token,
        token_type="Bearer"
    )


@router.delete("/sessions/")
async def logout(
    token: Annotated[str, Depends(oauth2_scheme)],
    session_user: Annotated[RowSessionUser, Depends(get_session_user)],
    cache_client: Annotated[ClientRedis, Depends(cache_helper.get_client)]
):
    return Response(status_code=status.HTTP_204_NO_CONTENT)