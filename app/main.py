import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import auth, post, user, vote

models.Base.metadata.create_all(bind=engine)

api = FastAPI(title="Social Media App")

origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(filename="logs/api.log", filemode="w", level=logging.INFO)

api.include_router(post.router)
api.include_router(user.router)
api.include_router(auth.router)
api.include_router(vote.router)


@api.get("/")
def root():
    return {"message": "Social Media App with Fast API"}
