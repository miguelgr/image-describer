#!/bin/bash
python manage.py migrate
celery -A image_describer worker -l INFO
