import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

database = os.environ["DATABASE"]
user = os.environ["DATABASE_USER"]
password = os.environ["DATABASE_PASSWORD"]
database_host = os.environ["DATABASE_HOST"]

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@ip_address/db"
SQLALCHEMY_DATABASE_URL: str = (
    f"postgresql://{user}:{password}@{database_host}/{database}"
)

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
