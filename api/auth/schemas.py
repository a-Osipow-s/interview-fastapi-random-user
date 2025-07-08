from typing import TypedDict
from pydantic import BaseModel


class SessionUser(TypedDict):
    id: int | None
    username: str | None
    email: str | None


class Token(BaseModel):
    access_token: str
    token_type: str
