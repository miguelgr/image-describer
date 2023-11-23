FROM python:3.11-slim as base

WORKDIR /app/

COPY config/requirements-base.txt requirements-base.txt
COPY config/requirements-dev.txt requirements-dev.txt

COPY manage.py /app/
COPY tests /app/tests
COPY image_describer /app/image_describer

CMD ["bash", "entrypoint.sh"]

FROM base as api

COPY config/api/entrypoint.sh /app/entrypoint.sh
COPY config/api/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements-dev.txt

EXPOSE 9000

FROM base as worker

COPY config/worker/entrypoint.sh /app/entrypoint.sh
COPY config/worker/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements-dev.txt
