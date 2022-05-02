import html
import os
from datetime import datetime

import pytest
from dotenv import load_dotenv
from py.xml import html

load_dotenv()


@pytest.fixture(scope="module")
def api_key() -> str:
    api_key = os.environ.get("OPENWEATHER_APIKEY")
    return f"appid={api_key}"


@pytest.fixture
def base_url() -> str:
    return "https://api.openweathermap.org/data/2.5/weather"


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("Description"))
    cells.insert(1, html.th("Time", class_="sortable time", col="time"))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
