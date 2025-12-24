import pytest
from utils.data_loader import load_csv
from utils.retry import retry

@retry(attempts=3, delay=2)
def test_basic_auth_success(api_client):
    response = api_client.get(
        f"{api_client.base_url}/basic-auth/user/pass",
        auth=("user", "pass")
    )

    assert response.status_code == 200
    assert response.json()["authenticated"] is True
