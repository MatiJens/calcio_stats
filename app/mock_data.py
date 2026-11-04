"""Mock data shaped like football-data.org API responses.

Replace these functions with real HTTP calls to
https://api.football-data.org/v4/... once an API key is available.
"""

COMPETITION = {
    "id": 2019,
    "name": "Serie A",
    "area": {"name": "Italy"},
    "currentSeason": {"startDate": "2024-08-17", "endDate": "2025-05-25"},
}

STANDINGS = [
    {"position": 1, "team": "Inter", "playedGames": 10, "won": 8, "draw": 1, "lost": 1, "points": 25},
    {"position": 2, "team": "Napoli", "playedGames": 10, "won": 7, "draw": 2, "lost": 1, "points": 23},
    {"position": 3, "team": "Atalanta", "playedGames": 10, "won": 6, "draw": 3, "lost": 1, "points": 21},
    {"position": 4, "team": "Juventus", "playedGames": 10, "won": 5, "draw": 4, "lost": 1, "points": 19},
    {"position": 5, "team": "Milan", "playedGames": 10, "won": 5, "draw": 2, "lost": 3, "points": 17},
]

LAST_RESULTS = [
    {
        "utcDate": "2024-11-02T19:45:00Z",
        "homeTeam": "Milan",
        "awayTeam": "Inter",
        "score": {"home": 1, "away": 2},
    },
    {
        "utcDate": "2024-11-02T17:00:00Z",
        "homeTeam": "Juventus",
        "awayTeam": "Napoli",
        "score": {"home": 0, "away": 0},
    },
    {
        "utcDate": "2024-11-01T19:45:00Z",
        "homeTeam": "Atalanta",
        "awayTeam": "Roma",
        "score": {"home": 3, "away": 1},
    },
]


def get_competition():
    return COMPETITION


def get_standings():
    return STANDINGS


def get_last_results():
    return LAST_RESULTS
