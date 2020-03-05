import sqlalchemy
import databases

database = databases.Database("postgresql://postgres:postgres@localhost:5432/mydb")
metadata = sqlalchemy.MetaData()
