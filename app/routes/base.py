from fastapi import APIRouter
from app.core.celery_app import celery_app

import sqlalchemy
from pathlib import Path
from openpyxl import load_workbook


from app.db.models import Base, Group, Period, ScheduleFile

router = APIRouter()


@router.get('/task_status/{task_id}')
def task_status(task_id):
    res = celery_app.AsyncResult(task_id)
    return {'state': res.state, 'info': res.info}



@router.get('/sometest')
async def creategroup():



    return "okk"
