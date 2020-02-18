from app.core.celery_app import celery_app
from app.core.config import MIREA_SCHEDULE_URL
from celery.result import AsyncResult
import os
import re
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from contextlib import contextmanager
from loguru import logger
import redis

from time import sleep

redis_client = redis.Redis(host='localhost', port=6379)


# https://docs.celeryproject.org/en/latest/userguide/tasks.html#avoid-launching-synchronous-subtasks
# exceptions https://www.distributedpython.com/2018/09/28/celery-task-states/
@celery_app.task(acks_late=True)
def test_celery(word: str):
    sleep(5)
    return f"test task return {word}"


@celery_app.task(bind=True, track_started=True)
def download_files(self):
    # folder = Path('schedule_files/unidentified')
    # os.makedirs(folder, exist_ok=True)
    #
    # s = requests.Session()
    # page = s.get(MIREA_SCHEDULE_URL)
    # soup = BeautifulSoup(page.text, "html.parser")
    # links = soup.findAll('a', attrs={'href': re.compile(".+(IIT|IK)\s*.*\.(xlsx)$")})
    #
    # for idx, link in enumerate(links):
    #     file_name = link.get('href').split('/')[-1]
    #     logger.info(f'{idx} {file_name}')
    #     r = s.get(link.get('href'), allow_redirects=True)
    #     p = Path(folder / file_name)
    #     open(p, 'wb').write(r.content)

    total = 10
    for i in range(total):
        logger.info(f'{i} {self.AsyncResult(self.request.id).state}')
        self.update_state(state='PROGRESS', meta={'done': i, 'total': total})
        sleep(2)
    logger.info(self.AsyncResult(self.request.id).state)
    return 'finished'
