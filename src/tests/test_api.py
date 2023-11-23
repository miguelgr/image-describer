import json

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_prediction_valid_image(test_client, base64_image):
    data = {"image": f"data:image/png;base64,{base64_image}"}
    response = test_client.post("/api/v1/predictions", data, format="json")
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_prediction_invalid_image(test_client):
    pass


def test_create_prediction_ok(test_client):
    pass


def test_create_prediction_ko(test_client):
    pass
