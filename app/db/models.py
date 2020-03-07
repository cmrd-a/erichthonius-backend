from sqlalchemy import Column, Integer, String, SmallInteger, Boolean, ForeignKey, DateTime, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    periods = relationship("Period", back_populates="group")


class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class ScheduleFile(Base):
    __tablename__ = "schedule_file"

    id = Column(Integer, primary_key=True)
    year = Column(SmallInteger)
    semester = Column(Boolean)
    institute = Column(String)
    grade = Column(String)
    course = Column(SmallInteger)
    category = Column(String)
    file_name = Column(String)
    updated = Column(DateTime)


class Period(Base):
    __tablename__ = "period"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="periods")
    weekday = Column(SmallInteger)
    number = Column(SmallInteger)
    even = Column(Boolean)
    name = Column(String)
    catgeory = Column(String)
    teacher = Column(Integer, ForeignKey('teacher.id'))
    room = Column(Integer, ForeignKey('room.id'))
    file = Column(Integer, ForeignKey('schedule_file.id'))

    month = Column(String)
    time = Column(Time)
    day = Column(SmallInteger)
