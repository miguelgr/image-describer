import pytest
from rest_framework.test import APIClient


@pytest.fixture
def test_client():
    yield APIClient()
