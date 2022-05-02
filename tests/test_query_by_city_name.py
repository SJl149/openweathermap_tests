import pytest

from helpers import get_current_weather

cities = [
    {"name": "London", "query": "London"},
    {"name": "London", "query": "London,uk"},
    {"name": "New York", "query": "New York"},
    {"name": "New York", "query": "New York,ny"},
    {"name": "New York", "query": "New York,ny,us"},
    {"name": "New York", "query": "New York,us"},
]


@pytest.mark.parametrize("city", cities)
def test_query_by_city_name(base_url: str, api_key: str, city: dict):
    formatted_city = f"q={city['name']}"
    status_code, response = get_current_weather(base_url=base_url, api_key=api_key, query_params=formatted_city)
    assert status_code == 200
    assert response["name"] == city["name"]
