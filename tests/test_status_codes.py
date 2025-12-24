import pytest
from utils.data_loader import load_csv
from utils.retry import retry

@pytest.mark.parametrize("code", [200, 201, 204])
@retry(attempts=3, delay=2)
def test_status_codes_success(api_client, code):
    response = api_client.get(f"{api_client.base_url}/status/{code}")
    assert response.status_code == code