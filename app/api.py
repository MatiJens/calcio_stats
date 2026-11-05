"""HTTP client for football-data.org v4 API.

Configuration via environment variables:
- FOOTBALL_DATA_API_KEY      (required to hit the real API)
- FOOTBALL_DATA_BASE_URL     (default: https://api.football-data.org/v4)
- FOOTBALL_DATA_COMPETITION  (default: SA — Serie A)

If FOOTBALL_DATA_API_KEY is not set, the module falls back to mock_data
so the app still runs locally without credentials.
"""

import os
import time
from typing import Any

import httpx

from app import mock_data

BASE_URL = os.getenv("FOOTBALL_DATA_BASE_URL", "https://api.football-data.org/v4")
API_KEY = os.getenv("FOOTBALL_DATA_API_KEY", "")
COMPETITION_CODE = os.getenv("FOOTBALL_DATA_COMPETITION", "SA")

CACHE_TTL_SECONDS = int(os.getenv("FOOTBALL_DATA_CACHE_TTL", "60"))
_cache: dict[str, tuple[float, Any]] = {}


def _use_mock() -> bool:
    return not API_KEY


def _get(path: str) -> dict:
    """GET with simple in-memory TTL cache."""
    now = time.time()
    cached = _cache.get(path)
    if cached and now - cached[0] < CACHE_TTL_SECONDS:
        return cached[1]

    headers = {"X-Auth-Token": API_KEY}
    with httpx.Client(base_url=BASE_URL, headers=headers, timeout=10.0) as client:
        response = client.get(path)
        response.raise_for_status()
        data = response.json()

    _cache[path] = (now, data)
    return data


def get_competition() -> dict:
    if _use_mock():
        return mock_data.get_competition()
    return _get(f"/competitions/{COMPETITION_CODE}")


def get_standings() -> list[dict]:
    if _use_mock():
        return mock_data.get_standings()
    data = _get(f"/competitions/{COMPETITION_CODE}/standings")
    for standing in data.get("standings", []):
        if standing.get("type") == "TOTAL":
            return standing.get("table", [])
    return []


def get_last_results() -> list[dict]:
    """Return matches from the most recent matchday that has finished games."""
    if _use_mock():
        matches = mock_data.get_last_results()
    else:
        data = _get(f"/competitions/{COMPETITION_CODE}/matches?status=FINISHED")
        matches = data.get("matches", [])

    if not matches:
        return []

    last_matchday = max(m.get("matchday") or 0 for m in matches)
    return [m for m in matches if m.get("matchday") == last_matchday]
