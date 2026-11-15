import redis.asyncio as redis



class RedisConnector:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.redis = None


    async def connect(self):
        self.redis = await redis.Redis(host=self.host, port=self.port)


    async def set(self, key: str, value: str, expire: int = None):
        if expire:
            await self.redis.set(key, value)
        else:
            await self.redis.set(key, value, expire)


    async def get(self, key: str):
        return await self.redis.get(key)


    async def delete(self, key: str):
        await self.redis.delete(key)


    async def close(self):
        if self.redis:
            await self.redis.close()