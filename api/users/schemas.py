from typing import Annotated

from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    username: Annotated[str, Field(max_length=40)]
    first_name: Annotated[str, Field(max_length=40)]
    last_name: Annotated[str, Field(max_length=40)]
    password: Annotated[str, Field(min_length=10, max_length=50)]
