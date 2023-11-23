import base64

import pytest
from rest_framework.test import APIClient


def encode_image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        binary_data = image_file.read()
        base64_encoded = base64.b64encode(binary_data)
        base64_string = base64_encoded.decode("utf-8")
    return base64_string


IMAGE_PATH = "../static/test_image.jpg"


@pytest.fixture
def test_client():
    yield APIClient()


@pytest.fixture
def base64_image():
    yield encode_image_to_base64(IMAGE_PATH)
