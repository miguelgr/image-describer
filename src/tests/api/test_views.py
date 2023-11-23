import json
from unittest import mock

import pytest
from rest_framework.test import APIClient


@mock.patch("image_describer.tasks.predict_image_title")
@pytest.mark.django_db
def test_create_prediction_valid_image(test_client, base64_image, predict_mock):
    data = {"image": f"data:image/png;base64,{base64_image}"}
    predict_mock.return_value = "image_title"

    response = test_client.post("/api/v1/predictions", data, format="json")

    assert predict_mock.called
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_prediction_invalid_image(test_client):
    pass


def test_create_prediction_ok(test_client):
    pass


def test_create_prediction_ko(test_client):
    pass
