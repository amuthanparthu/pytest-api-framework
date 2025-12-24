import os
import yaml

def load_config():
    with open("configs/config.yaml") as f:
        config = yaml.safe_load(f)

    config["base_url"] = os.getenv(
        "BASE_URL",
        "https://httpbin.org"
    )
    return config
  
