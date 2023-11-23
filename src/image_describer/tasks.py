import uuid
from datetime import datetime
from dataclasses import field, dataclass

from celery import shared_task

from django.conf import settings


@dataclass
class PredictionTask:
    id: field(default_factory=uuid.uuid4)
    timestamp: datetime = field(default_factory=datetime.now)
    content: str = ""


@dataclass
class PredictionTaskResult:
    id: field(default_factory=uuid.uuid4)
    timestamp: datetime = field(default_factory=datetime.now)
    value: str = ""


# Using a shared task Celery will automatically distribute the task to multiple workers.
# Celery tasks provide autoretry capabilities: backoff, jitter
@shared_task(expires=settings.REQUEST_TIMEOUT)
# def predict_image_title(task: PredictionTask) -> PredictionTaskResult:
def predict_image_title(image_content):
    # Code just executed by the worker, avoiding the import of tensorflow libs.
    from image_describer.services.inference import infere_image_title

    title = infere_image_title(image=image_content)
    return PredictionTaskResult(value=title)
