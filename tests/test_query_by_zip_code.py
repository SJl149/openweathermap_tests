import pytest

from helpers import get_current_weather

cities = [
    {"name": "Mountain View", "zipcode": "94040"},
    {"name": "New York", "zipcode": "10007"},
    {"name": "New York", "zipcode": "10007", "country": "us"},
    {"name": "Mountain View", "zipcode": "94040"},
    {"name": "Schenectady", "zipcode": "12345"},  # GE zipcode
    {"name": "Holtsville", "zipcode": "00501"},  # smallest zipcode
    {"name": "Ketchikan", "zipcode": "99950"},  # largest zipcode
    {"name": "Washington", "zipcode": "20252"},  # zipcode assigned to Smokey Bear
]


@pytest.mark.parametrize("city", cities, ids=[city["name"] for city in cities])
def test_query_by_zip_code(base_url: str, api_key: str, city: dict):
    formatted_city = f"zip={city['zipcode']}"
    if city.get("country"):
        formatted_city += f",{city['country']}"

    status_code, response = get_current_weather(base_url=base_url, api_key=api_key, query_params=formatted_city)
    assert status_code == 200, f"\nTest data: {city}\nResponse: {response}"
    assert response["name"] == city["name"], f"Expected: {response['name']}, Actual: {city['name']}"
