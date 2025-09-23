from beanie import PydanticObjectId, Document
from api.mixins.common import TimestampMixin

class UserMongo(Document, TimestampMixin):
    username: str

    class Settings:
        name = "user_mongo_collection"

