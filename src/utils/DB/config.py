from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USERNAME : str
    DB_PASSWORD : str
    DB_HOST : str 
    DB_PORT : int
    DB_DATABASE : str
    JWT_SECRET_KEY : str
    JWT_ALGORITHM : str

    DATABASE_URL : str
    class Config:
        env_file = ".env" 

settings = Settings()