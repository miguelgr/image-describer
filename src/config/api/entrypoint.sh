#!/bin/bash
# Development
python manage.py migrate
# python manage.py runserver 0.0.0.0:$PORT

# Production
# Handle concurrency with multiple workers
gunicorn image_describer.wsgi  -b 0.0.0.0:9000 --workers 4 --log-level info --timeout 90
