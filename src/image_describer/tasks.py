import uuid
from datetime import datetime

from celery import shared_task

from django.conf import settings


# Using a shared task Celery will automatically distribute the task to multiple workers.
# Celery tasks provide autoretry capabilities: backoff, jitter
@shared_task(expires=settings.REQUEST_TIMEOUT)
def predict_image_title(image_content):
    # Code just executed by the worker, avoiding the import of tensorflow libs.
    from image_describer.services.inference import inference_service

    title = inference_service.predict(image_content)
    return PredictionTaskResult(value=title)
