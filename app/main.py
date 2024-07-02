from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router
from models import Base
from database import engine

app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
