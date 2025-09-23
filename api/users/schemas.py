from pydantic import BaseModel, Field
from beanie import PydanticObjectId

class UserIn(BaseModel):
    username: str

    class Config:
        schema_extra = {
            "example": {
                "username": "john_doe"
            }
        }


class UserOut(BaseModel):
    id: PydanticObjectId
    username: str

    class Config:
        schema_extra = {
            "example": {
                "id": "dasdasdasdasd",
                "username": "john_doe"
            }
        }
