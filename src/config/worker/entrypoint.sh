#!/bin/bash
python manage.py migrate
# The number of worker processes/threads can be changed using the --concurrency argument and defaults to the number of CPUs available on the machine.
celery -A image_describer worker -l INFO
