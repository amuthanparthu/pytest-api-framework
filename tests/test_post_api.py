import pytest
from utils.data_loader import load_json
from utils.faker_utils import random_user

payloads = load_json("test_data/post_payloads.json")

@pytest.mark.parametrize("payload", payloads)
def test_post_data(api_client, payload):
    payload.update(random_user())

    response = api_client.post(
        f"{api_client.base_url}/post",
        json=payload
    )

    assert response.status_code == 200
    assert response.json()["json"]["name"] == payload["name"]
