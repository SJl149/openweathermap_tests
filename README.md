## Tests of openweathermap.org api

### Requirements:
- `python >= 3.8`
- `pytest` (tests developed with 7.1.2)
- `requests` (tests developed with 2.27.1)
- `openweathermap.org` account with API key sign up at: [openweathermap](https://openweathermap.org/current#zip)
- `python-dotenv` optional
- `pytest-html >= 3.1`

### How to run:

1. Create or activate a python environment [venv documentaion](https://docs.python.org/3/library/venv.html)
2. Install all requirements: `pip install requirements.txt`
3. Run tests:
```Python
# Individually
pytest tests/test_query_by_coordinates.py --html=reports/report.html --self-contained-html

# All tests
pytest tests/ --html=reports/report.html --self-contained-html
```

An HTML report will be generated in `reports/` that can be viewed in your browser.


#### Created by:
Scott Lenander