#! /usr/bin/env bash
set -e

python /backend/app/pre_start.py

#celery worker -A app.worker -l info -Q main-queue -c 1
watchmedo auto-restart --directory=/backend/app/ --pattern=*.py --recursive -- celery worker -A app.worker -l info -Q main-queue -c 1