import pytest
from rest_framework.exceptions import ValidationError

from django.conf import settings

from image_describer.api.serializers import (
    Base64ImageField,
    PredictionCreateSerializer
)


def test_prediction_create_serializer_valid(base64_image):
    serializer = PredictionCreateSerializer(data={"image": base64_image})
    assert serializer.is_valid()


def test_prediction_create_serializer_not_valid(base64_image):
    serializer = PredictionCreateSerializer(data={"image": ""})
    assert not serializer.is_valid()


def test_base64_image_field_valid_data(base64_image):
    pass
    data = f"data:image/png;base64,{base64_image}"
    field = Base64ImageField()
    result = field.to_internal_value(data)

    assert isinstance(result, ContentFile)
    assert result.name == "uploaded_image.png"


def test_base64_image_field_invalid_data():
    pass
    data = f"data:image/png;base64,{base64_image}"
    field = Base64ImageField()

    with pytest.raises(ValidationError):
        result = field.to_internal_value(data)
