from datetime import date
from typing import Any

import pandas as pd

from data_ingestion.config import CityConfig


def fetch_weather(
    city: CityConfig,
    start_date: date,
    end_date: date,
) -> list[dict[str, Any]]:
    """
    Fetch historical weather data for a city.

    Args:
        city: City configuration containing ID and coordinates.
        start_date: Beginning of the requested date range.
        end_date: End of the requested date range.

    Returns:
        A list of weather records.
    """
    raise NotImplementedError


def validate_records(
    records: list[dict[str, Any]],
) -> pd.DataFrame:
    """
    Validate and transform raw weather records.

    Args:
        records: Raw weather records returned by the ingestion layer.

    Returns:
        A validated pandas DataFrame.
    """
    raise NotImplementedError


def load_records(
    records: pd.DataFrame,
    connection: Any,
) -> int:
    """
    Load validated weather records into PostgreSQL.

    Args:
        records: Validated weather DataFrame.
        connection: Database connection.

    Returns:
        Number of records loaded.
    """
    raise NotImplementedError