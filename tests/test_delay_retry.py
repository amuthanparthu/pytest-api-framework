import pytest
from utils.data_loader import load_csv
from utils.retry import retry

@retry(attempts=3, delay=2)
def test_delay_response(api_client):
    response = api_client.get(f"{api_client.base_url}/delay/2")
    assert response.status_code == 200