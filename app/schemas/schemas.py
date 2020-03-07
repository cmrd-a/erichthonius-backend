from typing import List

from pydantic import BaseModel


class PeriodBase(BaseModel):
    name: str


class PeriodCreate(PeriodBase):
    pass


class Period(PeriodBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class GroupBase(BaseModel):
    name: str


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    periods: List[Period] = []

    class Config:
        orm_mode = True
