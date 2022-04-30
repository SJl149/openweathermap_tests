import pytest
from dotenv import load_dotenv
import os


load_dotenv()


@pytest.fixture(scope="module")
def api_key() -> str:
    api_key = os.environ.get("OPENWEATHER_APIKEY")
    return f"appid={api_key}"


@pytest.fixture
def base_url() -> str:
    return "https://api.openweathermap.org/data/2.5/weather"
