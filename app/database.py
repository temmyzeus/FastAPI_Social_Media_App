import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import db_config


# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@ip_address/db"
SQLALCHEMY_DATABASE_URL: str = f"postgresql://{db_config.DATABASE_USER}:{db_config.DATABASE_PASSWORD}@{db_config.DATABASE_HOST}/{db_config.DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
