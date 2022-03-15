import logging

from fastapi import FastAPI

from . import models
from .database import engine
from .routers import auth, post, user

models.Base.metadata.create_all(bind=engine)

api = FastAPI(title="Social Media App")
logging.basicConfig(filename="logs/api.log", filemode="w", level=logging.INFO)

api.include_router(post.router)
api.include_router(user.router)
api.include_router(auth.router)


@api.get("/")
def root():
    return {"message": "Social Media App with Fast API"}
