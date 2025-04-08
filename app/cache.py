from datetime import datetime, timedelta
from typing import Optional

CACHE_TTL_SECONDS = 300
cache = {}

def get_expiry(ttl: Optional[int]) -> datetime:
    return datetime.utcnow() + timedelta(seconds=ttl or CACHE_TTL_SECONDS)

def set_cache(key: str, data: dict):
    cache[key] = data

def pop_cache(key: str):
    return cache.pop(key, None)

def get_cache():
    return cache