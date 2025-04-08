import os
import asyncpg

POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql://user:password@db:5432/secrets")
db_pool = None

async def init_db():
    global db_pool
    db_pool = await asyncpg.create_pool(dsn=POSTGRES_DSN)
    async with db_pool.acquire() as conn:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id SERIAL PRIMARY KEY,
                secret_key TEXT,
                action TEXT,
                timestamp TIMESTAMP,
                ip TEXT,
                metadata JSONB
            );
        ''')