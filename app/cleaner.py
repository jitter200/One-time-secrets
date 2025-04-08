import asyncio
from datetime import datetime
from app.cache import get_cache

async def clear_expired():
    while True:
        now = datetime.utcnow()
        cache = get_cache()
        expired_keys = [k for k, v in cache.items() if v["expires_at"] < now]
        for k in expired_keys:
            cache.pop(k)
        await asyncio.sleep(60)

async def start_cleaner():
    asyncio.create_task(clear_expired())