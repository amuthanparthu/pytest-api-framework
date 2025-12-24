import pytest
from utils.data_loader import load_csv
from utils.retry import retry

test_data = load_csv("test_data/get_params.csv")

@pytest.mark.parametrize("row", test_data)
@retry(attempts=3, delay=2)
def test_get_with_params(api_client, row):
    response = api_client.get(
        f"{api_client.base_url}/get",
        params={row["param"]: row["value"]}
    )
    #print(response.json(), "res==")

    assert response.status_code == 200
    assert row["param"] in response.json()["args"]
    assert row["value"] == response.json()["args"][row['param']]
