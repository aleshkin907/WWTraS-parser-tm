from pydantic_settings import BaseSettings

class EnvSettings(BaseSettings):

    DATABASE_DIALECT: str
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_USERNAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

def get_env_variables():
    return EnvSettings()

