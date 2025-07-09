from typing import TypedDict, TypeAlias

from sqlalchemy.engine import Row

from pydantic import BaseModel


class SessionUser(TypedDict):
    id: int | None
    username: str | None
    email: str | None


RowSessionUser: TypeAlias = Row[SessionUser]


class TokenPayload(TypedDict):
    sub: int
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str
