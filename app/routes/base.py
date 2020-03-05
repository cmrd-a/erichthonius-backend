from fastapi import APIRouter
from app.core.celery_app import celery_app
from app.core.config import database, metadata
import sqlalchemy

from app.db.models import Group, Period

router = APIRouter()


@router.get('/task_status/{task_id}')
def task_status(task_id):
    res = celery_app.AsyncResult(task_id)
    return {'state': res.state, 'info': res.info}


@router.get('/initdb')
async def initdb():
    engine = sqlalchemy.create_engine(str(database.url))
    metadata.create_all(engine)
    return "okk"


@router.get('/creategroup')
async def creategroup():
    gr = await Group.objects.create(name="hikka12")
    await ScheduleFile.objects.create(groupe=gr)


    return "okk"
