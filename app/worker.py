import hashlib
import os
import re
from pathlib import Path
from time import sleep

import redis
import requests
from bs4 import BeautifulSoup
from loguru import logger

from app.core.celery_app import celery_app
from app.core.config import MIREA_SCHEDULE_URL

redis_client = redis.Redis(host='localhost', port=6379)


def md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# https://docs.celeryproject.org/en/latest/userguide/tasks.html#avoid-launching-synchronous-subtasks
# exceptions https://www.distributedpython.com/2018/09/28/celery-task-states/
@celery_app.task(acks_late=True)
def test_celery(word: str):
    sleep(5)
    return f"test task return {word}"


@celery_app.task(bind=True, track_started=True)
def download_files(self):
    folder = Path('schedule_files')
    os.makedirs(folder, exist_ok=True)

    session = requests.Session()
    page = session.get(MIREA_SCHEDULE_URL)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.findAll('a', attrs={'href': re.compile(".+(IIT|IK)\s*.*\.(xlsx)$")})
    total = len(links)
    for i, link in enumerate(links):
        file_name = link.get('href').split('/')[-1]
        # logger.info(f'{i} {file_name}')
        response = session.get(link.get('href'), allow_redirects=True)
        temp_path = Path(folder / file_name)
        open(temp_path, 'wb').write(response.content)
        md5hash = md5(temp_path)
        hash_path = Path(folder/md5hash).with_suffix('.xlsx')
        os.rename(temp_path, hash_path)
        self.update_state(state='PROGRESS', meta={'done': i + 1, 'total': total})
        sleep(1)
    logger.info(self.AsyncResult(self.request.id).state)
    return 'finished'


@celery_app.task(bind=True, track_started=True)
def identify_files(self):
    total = 5
    for i in range(total):
        logger.info(f'{i} {self.AsyncResult(self.request.id).state}')
        self.update_state(state='PROGRESS', meta={'done': i, 'total': total})
        sleep(2)
    logger.info(self.AsyncResult(self.request.id).state)
    return 'finished'
