import pytest

from helpers import get_current_weather

coordinates = [
    {"lat": 35, "lon": 139},
    {"lat": -16, "lon": 145},
    {"lat": -33, "lon": -70},
    {"lat": 40, "lon": -74},
    {"lat": -90, "lon": -180},
    {"lat": 90, "lon": 180},
    {"lat": 0, "lon": 0},
    {"lat": 51, "lon": 0},
    {"lat": 51.5, "lon": 0.1},
    {"lat": 51.51, "lon": 0.12},
    {"lat": 51.507, "lon": 0.127},
    {"lat": 51.5072, "lon": 0.1276},
]


@pytest.mark.parametrize("coordinates", coordinates, ids=[f"{item['lat']},{item['lon']}" for item in coordinates])
def test_query_by_coordinates(base_url: str, api_key: str, coordinates: dict):
    formatted_coordinates = f"lat={coordinates['lat']}&lon={coordinates['lon']}"
    status_code, response = get_current_weather(base_url=base_url, api_key=api_key, query_params=formatted_coordinates)
    assert status_code == 200, f"\nTest data: {coordinates}\nResponse: {response}"
    assert (
        response["coord"]["lat"] == coordinates["lat"]
    ), f"Expected: {coordinates['lat']}, Actual: {response['coord']['lat']}"
    assert (
        response["coord"]["lon"] == coordinates["lon"]
    ), f"Expected: {coordinates['lon']}, Actual: {response['coord']['lon']}"
