FROM python:3.8

COPY poetry.lock pyproject.toml /backend/

WORKDIR /backend/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

ENV PYTHONPATH=/backend