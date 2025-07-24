from typing import TypedDict, TypeAlias

from sqlalchemy.engine import Row

from pydantic import BaseModel, EmailStr


class SessionUser(TypedDict):
    id: int | None
    username: str | None
    email: str | None


RowSessionUser: TypeAlias = Row[SessionUser]


class TokenPayload(TypedDict):
    sub: str
    id: int
    email: EmailStr
    exp: int
    iat: int


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginForm(BaseModel):
    username: str
    password: str
