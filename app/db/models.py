from app.core.config import database, metadata
import orm


class Group(orm.Model):
    __tablename__ = "group"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    name = orm.String(max_length=256, unique=True)


class Teacher(orm.Model):
    __tablename__ = "teacher"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    name = orm.String(max_length=256, unique=True)


class Room(orm.Model):
    __tablename__ = "room"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    name = orm.String(max_length=256, unique=True)


class ScheduleFile(orm.Model):
    __tablename__ = "schedule_file"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    semester = orm.Boolean()
    grade = orm.String(max_length=256)
    year = orm.String(max_length=256)
    category = orm.String(max_length=256)
    institute = orm.String(max_length=256)
    course = orm.String(max_length=256)
    file_name = orm.String(max_length=256)
    updated = orm.DateTime()


class Period(orm.Model):
    __tablename__ = "period"
    __database__ = database
    __metadata__ = metadata

    id = orm.Integer(primary_key=True)
    group = orm.ForeignKey(Group)
    weekday = orm.String(max_length=256)
    number = orm.String(max_length=256)
    even = orm.Boolean()
    names = orm.String(max_length=256)
    catgeory = orm.String(max_length=256)
    teacher = orm.ForeignKey(Teacher)
    room = orm.ForeignKey(Room)
    file = orm.ForeignKey(ScheduleFile)

    month = orm.String(max_length=256)
    time = orm.Time()
    day = orm.Integer()
