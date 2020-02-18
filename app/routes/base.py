from fastapi import APIRouter
from app.core.celery_app import celery_app

router = APIRouter()


@router.get('/task_status/{task_id}')
def task_status(task_id):
    res = celery_app.AsyncResult(task_id)
    return {'state': res.state, 'info': res.info}
