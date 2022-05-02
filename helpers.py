from typing import Tuple

import requests


def get_current_weather(base_url: str, api_key: str, query_params: str) -> Tuple[int, str]:
    r = requests.get(f"{base_url}?{query_params}&{api_key}")
    return r.status_code, r.json()
