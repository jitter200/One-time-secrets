from datetime import datetime
from app.db import db_pool

async def log_action(secret_key: str, action: str, ip: str, metadata: dict = None):
    async with db_pool.acquire() as conn:
        await conn.execute("""
            INSERT INTO logs (secret_key, action, timestamp, ip, metadata)
            VALUES ($1, $2, $3, $4, $5);
        """, secret_key, action, datetime.utcnow(), ip, metadata)