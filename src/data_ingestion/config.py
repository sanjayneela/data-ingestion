from dataclasses import dataclass


@dataclass(frozen=True)
class CityConfig:
    city_id: str
    name: str
    latitude: float
    longitude: float


CITIES = {
    "omaha": CityConfig(
        city_id="omaha",
        name="Omaha",
        latitude=41.2565,
        longitude=-95.9345,
    ),
    "new_york": CityConfig(
        city_id="new_york",
        name="New York",
        latitude=40.7128,
        longitude=-74.0060,
    ),
    "hyderabad": CityConfig(
        city_id="hyderabad",
        name="Hyderabad",
        latitude=17.3850,
        longitude=78.4867,
    ),
}


TIMEZONE = "UTC"

START_DATE = "2025-01-01"
END_DATE = "2025-01-07"