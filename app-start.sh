#! /usr/bin/env bash

# Let the DB start
python /backend/app/pre_start.py

# Run migrations
alembic upgrade head

uvicorn --host=0.0.0.0 app.main:app --reload