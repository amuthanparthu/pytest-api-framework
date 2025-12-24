import pytest
import requests
from utils.config_loader import load_config

@pytest.fixture(scope="session")
def api_client():
    config = load_config()
    session = requests.Session()
    session.base_url = config["base_url"]
    return session
