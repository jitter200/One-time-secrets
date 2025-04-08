from fastapi import FastAPI
from app.routes import router
from app.cleaner import start_cleaner
from app.db import init_db

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def on_startup():
    await init_db()
    await start_cleaner()