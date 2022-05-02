import pytest

from helpers import get_current_weather

cities = [
    {"name": "London", "query": ["London"]},
    {"name": "London", "query": ["London", "uk"]},
    {"name": "New York", "query": ["New York City"]},
    {"name": "New York", "query": ["New York City", "ny"]},
    {"name": "New York", "query": ["New York", "ny", "us"]},
    {"name": "New York", "query": ["New York", "us"]},
    {"name": "Tokyo", "query": ["Tokyo"]},
    {"name": "Tokyo", "query": ["Tokyo", "jp"]},
    {"name": "Shanghai", "query": ["Shanghai"]},
    {"name": "Shanghai", "query": ["Shanghai", "cn"]},
    {"name": "Mexico City", "query": ["Mexico City"]},
    {"name": "Mexico City", "query": ["Mexico City", "mx"]},
    {"name": "Truth or Consequences", "query": ["Truth or Consequences"]},
    {"name": "Truth or Consequences", "query": ["Truth or Consequences", "us"]},
    {
        "name": "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch",
        "query": ["Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"],
    },
    {
        "name": "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch",
        "query": ["Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch", "gb"],
    },
]


@pytest.mark.parametrize("city", cities, ids=[city["name"] for city in cities])
def test_query_by_city_name(base_url: str, api_key: str, city: dict):
    formatted_city = f"q={','.join(city['query'])}"
    status_code, response = get_current_weather(base_url=base_url, api_key=api_key, query_params=formatted_city)
    assert status_code == 200, f"\nTest data: {city}\nResponse: {response}"
    assert response["name"] == city["name"], f"Expected: {city['name']}, Actual: {response['name']}"
