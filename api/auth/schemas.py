from pydantic import BaseModel


class UserAuthSchema(BaseModel):
    id: int
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
