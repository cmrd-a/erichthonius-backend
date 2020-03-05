import os
from starlette.config import Config
import sqlalchemy
import databases

database = databases.Database("postgresql://postgres:postgres@localhost:5432/mydb")
metadata = sqlalchemy.MetaData()


config = Config(".env")

POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}"
)

MIREA_SCHEDULE_URL: str = config("MIREA_SCHEDULE_URL")
