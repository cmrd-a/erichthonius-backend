from app.db.config import database, metadata
import orm


class Group(orm.Model):
    __tablename__ = "group"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    name = orm.String(max_length=100)




