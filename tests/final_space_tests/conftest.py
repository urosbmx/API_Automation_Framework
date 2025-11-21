import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    """
    Returns the base URL of the Final Space API from .env
    """
    return "https://finalspaceapi.com/api/v0/episode/"
