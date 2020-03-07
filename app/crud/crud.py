from sqlalchemy.orm import Session

from app.schemas import schemas
from app.db import models


def get_group(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()


def get_group_by_name(db: Session, name: str):
    return db.query(models.Group).filter(models.Group.name == name).first()


def get_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Group).offset(skip).limit(limit).all()


def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def create_group_period(db: Session, period: schemas.PeriodCreate, group_id: int):
    db_period = models.Period(**period.dict(), group_id=group_id)
    db.add(db_period)
    db.commit()
    db.refresh(db_period)
    return db_period
