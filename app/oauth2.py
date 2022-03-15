import os
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from . import schemas, models
from .database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECERT_KEY: str = os.environ["SECERT_KEY"]
ALGORITHM: str = os.environ["ALGORITHM"]
ACCESS_TOKEN_EXPIRATION_TIME_IN_MINUES: int = int(
    os.environ["ACCESS_TOKEN_EXPIRATION_TIME_IN_MINUES"]
)


def create_access_token(data):
    to_encode = data.copy()
    to_expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRATION_TIME_IN_MINUES
    )
    to_encode.update({"exp": to_expire})
    encoded_jwt_token = jwt.encode(to_encode, key=SECERT_KEY, algorithm=ALGORITHM)
    return encoded_jwt_token


def verify_access_token(token: str, credentials_exception):
    try:
        payload: dict = jwt.decode(token, key=SECERT_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")

        if not user_id:
            raise credentials_exception

        token_data = schemas.TokenData(id=user_id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token_data.id).first()
    return user
