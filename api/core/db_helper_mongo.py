from beanie import init_beanie
from decouple import config
import motor.motor_asyncio

from api.models.user_mongo import UserMongo

MONGO_DETAILS = config("MONGO_DETAILS")


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
    document_models = [UserMongo]

    await init_beanie(
        database=client.get_default_database(),
        document_models=document_models
    )
