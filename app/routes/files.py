from fastapi import APIRouter, BackgroundTasks
from app.core.celery_app import celery_app
from app.worker import download_files, identify_files

router = APIRouter()


@router.get('/')
async def read_root():
    return {'Hello': 'World'}


@router.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}


@router.get('/books')
async def ping_pong():
    return {
        'status': 'success',
        'books': 'BOOKS'
    }


@router.get('/files')
async def files():
    return {
        'status': 'success',
        'books': 'BOOKS'
    }


@router.post('/books')
async def books(title: str, author: str, read: bool):
    return {
        'status': 'success',
        'message': 'Book added!'
    }


@router.post("/test-celery/", status_code=201)
def test_celery():
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.test_celery", args=['szaa----'])
    return {"msg": "Word received"}


@router.get('/download')
def download():
    result = download_files.delay()
    return {'msg': 'dl start', 'task_id': result.task_id}


@router.get('/identify')
def identify():
    result = identify_files.delay()
    return {'msg': 'dl start', 'task_id': result.task_id}
