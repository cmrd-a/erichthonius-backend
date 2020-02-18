FROM python:3.8


ENV C_FORCE_ROOT=1\
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

COPY poetry.lock pyproject.toml /backend/

WORKDIR /backend

RUN pip install "poetry==1.0.3" && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

ENV PYTHONPATH=/backend

COPY ./worker-start.sh /worker-start.sh

RUN chmod +x /worker-start.sh

CMD ["bash", "/worker-start.sh"]
