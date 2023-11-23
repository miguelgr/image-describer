import sys
import base64
import logging

from rest_framework import serializers

from django.conf import settings


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        max_size = settings.MAX_REQUEST_IMAGE_SIZE
        imgstr = data
        # Assumes the data is in the format 'data:image/png;base64,iVBORw0KG...'
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(";base64,")
        try:
            binary_data = base64.b64decode(imgstr)
            size_in_bytes = sys.getsizeof(binary_data)
        except Exception as e:
            raise ValidationError("Invalid base64-encoded string") from e

        if size_in_bytes > max_size:
            logging.info("Max image size exceeded")
            raise ValidationError(
                "Maximun image size exceeded, {max_size / 1024 / 1024} MB"
            ) from e

        return super().to_internal_value(data)


class PredictionCreateSerializer(serializers.Serializer):
    image = Base64ImageField(max_length=None, use_url=True)
