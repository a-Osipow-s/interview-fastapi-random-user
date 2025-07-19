from redis.asyncio import Redis
from redis.asyncio.client import Redis as ClientRedis

from pydantic import RedisDsn

from api.core.config import settings


class CacheHelper:

    def __init__(
        self, 
        url: RedisDsn, 
        decode_responses: bool = True
    ) -> None:
        self.client = Redis.from_url(
            url=url, 
            decode_responses=decode_responses
        )
    
    async def get_client(self) -> ClientRedis:
        return await self.client
    
    async def aclose(self) -> None:
        await self.client.aclose()

cache_helper = CacheHelper(str(settings.redis.url), True)