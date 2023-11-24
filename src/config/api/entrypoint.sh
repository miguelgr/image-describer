#!/bin/bash
# Development
python manage.py migrate
python manage.py runserver 0.0.0.0:$PORT

# Production
# default to avialable workers
#gunicorn image_describer.wsgi --workers 4
