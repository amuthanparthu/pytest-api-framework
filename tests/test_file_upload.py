import pytest
from utils.data_loader import load_csv
from utils.retry import retry

@retry(attempts=3, delay=2)
def test_file_upload(api_client, tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("pytest upload")

    with open(file_path, "rb") as f:
        response = api_client.post(
            f"{api_client.base_url}/post",
            files={"file": f}
        )

    assert response.status_code == 200
