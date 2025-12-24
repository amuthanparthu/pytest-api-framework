import pytest
from utils.data_loader import load_csv
from utils.retry import retry

@retry(attempts=3, delay=2)
def test_redirect(api_client):
    response = api_client.get(
        f"{api_client.base_url}/redirect/3",
        allow_redirects=True
    )

    assert response.history
    assert response.status_code == 200