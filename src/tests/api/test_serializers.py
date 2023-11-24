import pytest
from rest_framework.exceptions import ValidationError

from django.conf import settings

from image_describer.api.serializers import (
    Base64ImageField,
    PredictionCreateSerializer
)


def test_prediction_create_serializer_valid(base64_image):
    image_data = f"data:image/png;base64,{base64_image}"
    serializer = PredictionCreateSerializer(data={"image": image_data})
    assert serializer.is_valid()


def test_prediction_create_serializer_not_valid(base64_image):
    data = f"data:image/png;base64,base64_image"
    serializer = PredictionCreateSerializer(data={"image": data})
    assert not serializer.is_valid()


def test_prediction_create_serializer_not_valid_format_raise(base64_image):
    data = f"data:image/png;base64,base64_image"
    serializer = PredictionCreateSerializer(data={"image": data})
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)


def test_prediction_create_serializer_max_size_raise(create_image):
    image = create_image(settings.MAX_REQUEST_IMAGE_SIZE + 100)
    data = f"data:image/png;base64,{image}"
    serializer = PredictionCreateSerializer(data={"image": data})
    try:
        serializer.is_valid(raise_exception=True)
    except ValidationError as errors:
        assert "image size" in errors.detail["image"][0]


def test_prediction_create_serializer_image_field_content(base64_image):
    data = f"data:image/png;base64,{base64_image}"
    serializer = PredictionCreateSerializer(data={"image": data})
    serializer.is_valid(raise_exception=True)

    assert not serializer.validated_data["image"].startswith("data:image/png;base64,")
