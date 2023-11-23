FROM python:3.11-slim

WORKDIR /app

COPY requirements-dev.txt requirements-dev.txt
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY image_describer /app

EXPOSE 9000

COPY manage.py /app/
COPY entrypoint.sh /app/

CMD ["bash", "entrypoint.sh"]
