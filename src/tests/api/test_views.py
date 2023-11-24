import json
from unittest import mock

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
@mock.patch("image_describer.api.views.tasks")
def test_create_prediction_status_ok(tasks_mock, test_client, base64_image):
    data = {"image": f"data:image/png;base64,{base64_image}"}
    response = test_client.post("/api/v1/predictions", data, format="json")
    # task_result = mock.MagicMock()
    # task = mock.MagicMock()
    # tasks_mock.predict_image_title.delay.return_value = task
    # task.get.return_value = task_result
    # task_result.ok = True
    # task_result.value = 'title'
    assert tasks_mock.predict_image_title.delay.called
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_prediction_invalid_method_get(test_client):
    response = test_client.get("/api/v1/predictions")

    assert response.status_code == 405
