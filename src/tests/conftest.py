import io
import base64

import pytest
from PIL import Image
from rest_framework.test import APIClient


def generate_base64_image(size_in_bytes):
    return base64.b64encode(bytearray(size_in_bytes)).decode("utf-8")


def encode_image_file_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        binary_data = image_file.read()
        base64_encoded = base64.b64encode(binary_data)
        base64_string = base64_encoded.decode("utf-8")
    return base64_string


IMAGE_PATH = "tests/static/test_image.jpg"


@pytest.fixture
def test_client():
    yield APIClient()


@pytest.fixture(scope="session")
def base64_image():
    yield encode_image_file_to_base64(IMAGE_PATH)


@pytest.fixture()
def create_image():
    yield generate_base64_image
