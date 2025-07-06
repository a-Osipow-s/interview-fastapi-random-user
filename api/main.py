from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.core.db_helper import db_helper

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()

app: FastAPI = FastAPI(lifespan=lifespan)


@app.get('/')
async def root():
    return {"message": "Hello world!"}

@app.get('/test')
async def test():
    return {"message": "test"}