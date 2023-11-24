import os

from celery import Celery, signals

from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "image_describer.settings")

app = Celery("image_describer")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@signals.worker_init.connect
def init_worker(**kwargs):
    from image_describer.services.inference import inference_service
    inference_service.load_model(settings.DEFAULT_IMAGE_TO_TEXT_MODEL)
