import pytest

from helpers import get_current_weather

cities = [
    {"name": "Mountain View", "zipcode": "94040"},
    {"name": "New York", "zipcode": "10007"},
    {"name": "New York", "zipcode": "10007", "country": "us"},
    {"name": "Mountain View", "zipcode": "94040"},
]


@pytest.mark.parametrize("city", cities)
def test_query_by_zip_code(base_url: str, api_key: str, city: dict):
    formatted_city = f"zip={city['zipcode']}"
    if city.get("country"):
        formatted_city += f",{city['country']}"

    status_code, response = get_current_weather(base_url=base_url, api_key=api_key, query_params=formatted_city)
    assert status_code == 200
    assert response["name"] == city["name"]
