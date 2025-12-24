import pytest
from utils.data_loader import load_csv
from utils.retry import retry

@retry(attempts=3, delay=2)
def test_cookies(api_client):
    response = api_client.get(
        f"{api_client.base_url}/cookies/set/testcookie/value"
    )
    cookies_response = api_client.get(
        f"{api_client.base_url}/cookies"
    )
    assert cookies_response.json()["cookies"]["testcookie"] == "value"
