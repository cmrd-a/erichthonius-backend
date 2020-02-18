from celery import Celery

celery_app = Celery(
    'worker',
    broker='amqp://guest@queue.localhost//',
    backend='rpc://'
)

celery_app.conf.task_routes = {
    'app.worker.*': 'main-queue',
}