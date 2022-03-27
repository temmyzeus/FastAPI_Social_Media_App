from pydantic import BaseSettings


class DatabaseConfig(BaseSettings):
    DATABASE: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int

    class Config:
        env_file = ".env"


class AuthenticationConfig(BaseSettings):
    SECERT_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRATION_TIME_IN_MINUES: int

    class Config:
        env_file = ".env"


db_config = DatabaseConfig()
auth_config = AuthenticationConfig()
