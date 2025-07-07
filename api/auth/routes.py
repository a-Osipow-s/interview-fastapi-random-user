from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from api.auth import utils
from api.auth.schemas import UserAuthSchema, Token

router = APIRouter(prefix="/auth", tags=["AUTH"])


@router.post("/sessions/")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    # https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#update-the-dependencies
    # jwt_payload = {
    #     "sub": user_auth.id,
    #     "username": user_auth.username
    # }
    # access_token = utils.encode_jwt(jwt_payload)
    # return Token(
    #     access_token=access_token,
    #     token_type="Bearer"
    # )
    pass

@router.delete("/sessions/")
async def logout():
    # revoked token, add to blacklist
    pass