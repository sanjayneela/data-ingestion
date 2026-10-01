# Data Ingestion

A Python-based weather data ingestion project using Open-Meteo historical weather data.

## Project Scope

The initial project scope includes:

* Python
* PostgreSQL
* Docker Compose
* pandas
* requests
* pytest
* Streamlit
* GitHub Actions

Cloud services, Kafka, Airflow, and model training are outside the scope of this initial implementation.

## Configured Cities

The project is configured for:

* Omaha
* New York
* Hyderabad

Each city has an explicit city ID and geographic coordinates. Dates are handled using UTC.

## Interfaces

The project defines interfaces for the main ingestion workflow:

* `fetch_weather` — retrieves weather data.
* `validate_records` — validates weather records.
* `load_records` — loads validated records into the target data store.

These interfaces provide the contract that future implementations will follow.

## Testing

The project uses `pytest` for automated tests.

Run the test suite with:

```bash
pytest -v
```

The tests currently verify:

* City configuration
* City IDs
* UTC configuration
* Weather fixture structure
* Required cities in the fixture

## Branch and Pull Request Workflow

1. Create a small branch for each GitHub issue.
2. Link the relevant issue in the Pull Request.
3. Make only the changes required for the issue.
4. Run the test suite before pushing.
5. Push the branch to GitHub.
6. Open a Pull Request.
7. A teammate reviews the Pull Request.
8. Merge only after teammate review and approval.

## Current Branch

The current work is being completed on:

`issue-15-python-scaffold`

Related issue:

`#15`
