import base64

from rest_framework import serializers

from django.core.files.base import ContentFile


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith("data:image"):
            format, imgstr = data.split(
                ";base64,"
            )  # Assumes the data is in the format 'data:image/png;base64,iVBORw0KG...'
            ext = format.split("/")[-1]  # Extract the file extension
            data = ContentFile(base64.b64decode(imgstr), name=f"uploaded_image.{ext}")

        return super(Base64ImageField, self).to_internal_value(data)


class PredictionCreateSerializer(serializers.Serializer):
    image = Base64ImageField(max_length=None, use_url=True)
