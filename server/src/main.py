from fastapi import FastAPI, HTTPException, Depends
from src.config.database import engine, metadata
from src.routes.user import user

app = FastAPI()

app.include_router(user)