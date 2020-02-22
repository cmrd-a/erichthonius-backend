from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()


# todo: () return current semester, week, category

class Periods(BaseModel):
    year: int = datetime.today().year
    semester: int = 1
    category: int = 1
    week: int = 1


@router.post('/test/')
async def get_periods(periods: Periods):
    return periods
