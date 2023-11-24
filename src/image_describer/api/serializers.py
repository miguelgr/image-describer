import sys
import base64
import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.conf import settings


class Base64ImageField(serializers.CharField):
    def to_internal_value(self, data):
        # Assumes the data is in the format 'data:image/png;base64,iVBORw0KG...'
        max_size = settings.MAX_REQUEST_IMAGE_SIZE
        imgstr = data
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
        try:
            binary_data = base64.b64decode(imgstr)
            size_in_bytes = sys.getsizeof(binary_data)
        except Exception as exc:
            raise ValidationError("Invalid base64-encoded string") from exc
        if size_in_bytes > max_size:
            logging.info("Max image size exceeded %d", (size_in_bytes / 1024) / 1024)
            raise ValidationError(
                f"Maximum image size exceeded, {(max_size / 1024) / 1024} MB"
            )
        return super().to_internal_value(imgstr)


class PredictionCreateSerializer(serializers.Serializer):
    image = Base64ImageField(max_length=None)
