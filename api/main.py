from contextlib import asynccontextmanager
from fastapi import FastAPI

# from api.core.db_helper import db_helper
# from api.core.cache_helper import cache_helper

from api.users.routes import router as users_router

from api.core.db_helper_mongo import init_db
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    # await db_helper.dispose()
    # await cache_helper.aclose()

app: FastAPI = FastAPI(
    lifespan=lifespan,
    swagger_ui_parameters={
        'defaultModelsExpandDepth': -1,
    }
)

app.include_router(users_router)
