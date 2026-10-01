import json
from pathlib import Path


FIXTURE_FILE = (
    Path(__file__).parent
    / "fixtures"
    / "weather_records.json"
)


def test_weather_fixture():
    with FIXTURE_FILE.open() as file:
        records = json.load(file)

    assert len(records) == 3

    required_fields = {
        "city_id",
        "observed_at",
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation",
    }

    for record in records:
        assert required_fields.issubset(record.keys())


def test_fixture_contains_all_cities():
    with FIXTURE_FILE.open() as file:
        records = json.load(file)

    city_ids = {record["city_id"] for record in records}

    assert city_ids == {
        "omaha",
        "new_york",
        "hyderabad",
    }