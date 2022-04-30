import pytest
from helpers import get_current_weather


coordinates = [{"lat": 35, "lon": 139}, {"lat": -16, "lon": 145}]


@pytest.mark.parametrize("coordinates", coordinates)
def test_query_by_coordinates(base_url: str, api_key: str, coordinates: dict):
    formatted_coordinates = f"lat={coordinates['lat']}&lon={coordinates['lon']}"
    status_code, response = get_current_weather(base_url=base_url, api_key=api_key, query_params=formatted_coordinates)
    assert status_code == 200
    assert response["coord"]["lat"] == coordinates["lat"]
    assert response["coord"]["lon"] == coordinates["lon"]
