from typing import List, Optional

from beanie import PydanticObjectId

from api.users.schemas import UserIn, UserOut
from api.models.user_mongo import UserMongo


class UserService:
    async def list_users(self) -> List[UserMongo]:
        return await UserMongo.find_all().to_list()

    async def get_user(self, user_id: PydanticObjectId) -> Optional[UserMongo]:
        return await UserMongo.get(user_id)

    async def create_user(self, user_in: UserIn) -> UserMongo:
        user_db = UserMongo(**user_in.model_dump())
        return await user_db.insert()

    async def update_user(self, user_id: PydanticObjectId, user_in: UserIn) -> Optional[UserMongo]:
        user = await UserMongo.get(user_id)
        if not user:
            return
        return await user.set({"username": user_in.username})
        
    async def delete_user(self, user_id: PydanticObjectId) -> bool:
        user = await UserMongo.get(user_id)
        if not user:
            return
        return await user.delete()
        
user_service = UserService()

