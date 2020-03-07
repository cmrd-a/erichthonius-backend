import os
from starlette.config import Config


config = Config(".env")

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/mydb"

POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

MIREA_SCHEDULE_URL: str = config("MIREA_SCHEDULE_URL")
