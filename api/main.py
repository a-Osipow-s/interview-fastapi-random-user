from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.core.db_helper import db_helper

from api.users.routes import router as users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()

app: FastAPI = FastAPI(lifespan=lifespan)

app.include_router(users_router)
