from data_ingestion.config import CITIES, TIMEZONE


def test_three_cities_are_configured():
    assert set(CITIES.keys()) == {
        "omaha",
        "new_york",
        "hyderabad",
    }


def test_city_ids_are_explicit():
    assert CITIES["omaha"].city_id == "omaha"
    assert CITIES["new_york"].city_id == "new_york"
    assert CITIES["hyderabad"].city_id == "hyderabad"


def test_timezone_is_utc():
    assert TIMEZONE == "UTC"