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
    {"position": 1, "team": {"id": 505, "name": "Inter", "shortName": "Inter", "tla": "INT"}, "playedGames": 10, "form": "W,W,W,D,W", "won": 8, "draw": 1, "lost": 1, "points": 25, "goalsFor": 24, "goalsAgainst": 9, "goalDifference": 15},
    {"position": 2, "team": {"id": 113, "name": "Napoli", "shortName": "Napoli", "tla": "NAP"}, "playedGames": 10, "form": "W,W,D,W,W", "won": 7, "draw": 2, "lost": 1, "points": 23, "goalsFor": 20, "goalsAgainst": 8, "goalDifference": 12},
    {"position": 3, "team": {"id": 102, "name": "Atalanta", "shortName": "Atalanta", "tla": "ATA"}, "playedGames": 10, "form": "W,D,W,W,W", "won": 6, "draw": 3, "lost": 1, "points": 21, "goalsFor": 22, "goalsAgainst": 12, "goalDifference": 10},
    {"position": 4, "team": {"id": 109, "name": "Juventus", "shortName": "Juventus", "tla": "JUV"}, "playedGames": 10, "form": "D,W,D,W,W", "won": 5, "draw": 4, "lost": 1, "points": 19, "goalsFor": 16, "goalsAgainst": 7, "goalDifference": 9},
    {"position": 5, "team": {"id": 98, "name": "Milan", "shortName": "Milan", "tla": "MIL"}, "playedGames": 10, "form": "W,L,W,W,D", "won": 5, "draw": 2, "lost": 3, "points": 17, "goalsFor": 18, "goalsAgainst": 13, "goalDifference": 5},
    {"position": 6, "team": {"id": 100, "name": "Roma", "shortName": "Roma", "tla": "ROM"}, "playedGames": 10, "form": "W,D,W,L,W", "won": 5, "draw": 2, "lost": 3, "points": 17, "goalsFor": 15, "goalsAgainst": 12, "goalDifference": 3},
    {"position": 7, "team": {"id": 99, "name": "Fiorentina", "shortName": "Fiorentina", "tla": "FIO"}, "playedGames": 10, "form": "W,W,L,D,W", "won": 5, "draw": 1, "lost": 4, "points": 16, "goalsFor": 17, "goalsAgainst": 14, "goalDifference": 3},
    {"position": 8, "team": {"id": 103, "name": "Lazio", "shortName": "Lazio", "tla": "LAZ"}, "playedGames": 10, "form": "L,W,W,D,L", "won": 4, "draw": 3, "lost": 3, "points": 15, "goalsFor": 16, "goalsAgainst": 13, "goalDifference": 3},
    {"position": 9, "team": {"id": 586, "name": "Bologna", "shortName": "Bologna", "tla": "BOL"}, "playedGames": 10, "form": "D,W,D,W,L", "won": 4, "draw": 3, "lost": 3, "points": 15, "goalsFor": 13, "goalsAgainst": 12, "goalDifference": 1},
    {"position": 10, "team": {"id": 450, "name": "Torino", "shortName": "Torino", "tla": "TOR"}, "playedGames": 10, "form": "W,D,L,W,D", "won": 4, "draw": 2, "lost": 4, "points": 14, "goalsFor": 12, "goalsAgainst": 13, "goalDifference": -1},
    {"position": 11, "team": {"id": 108, "name": "Udinese", "shortName": "Udinese", "tla": "UDI"}, "playedGames": 10, "form": "L,W,D,L,W", "won": 4, "draw": 1, "lost": 5, "points": 13, "goalsFor": 12, "goalsAgainst": 15, "goalDifference": -3},
    {"position": 12, "team": {"id": 107, "name": "Genoa", "shortName": "Genoa", "tla": "GEN"}, "playedGames": 10, "form": "D,L,W,D,L", "won": 3, "draw": 3, "lost": 4, "points": 12, "goalsFor": 11, "goalsAgainst": 14, "goalDifference": -3},
    {"position": 13, "team": {"id": 115, "name": "Empoli", "shortName": "Empoli", "tla": "EMP"}, "playedGames": 10, "form": "L,D,W,L,D", "won": 3, "draw": 3, "lost": 4, "points": 12, "goalsFor": 9, "goalsAgainst": 12, "goalDifference": -3},
    {"position": 14, "team": {"id": 445, "name": "Cagliari", "shortName": "Cagliari", "tla": "CAG"}, "playedGames": 10, "form": "W,L,L,D,W", "won": 3, "draw": 2, "lost": 5, "points": 11, "goalsFor": 11, "goalsAgainst": 16, "goalDifference": -5},
    {"position": 15, "team": {"id": 104, "name": "Cremonese", "shortName": "Cremonese", "tla": "CRE"}, "playedGames": 10, "form": "L,D,L,W,D", "won": 2, "draw": 4, "lost": 4, "points": 10, "goalsFor": 10, "goalsAgainst": 14, "goalDifference": -4},
    {"position": 16, "team": {"id": 470, "name": "Frosinone", "shortName": "Frosinone", "tla": "FRO"}, "playedGames": 10, "form": "L,L,D,W,L", "won": 2, "draw": 3, "lost": 5, "points": 9, "goalsFor": 9, "goalsAgainst": 16, "goalDifference": -7},
    {"position": 17, "team": {"id": 488, "name": "Lecce", "shortName": "Lecce", "tla": "LEC"}, "playedGames": 10, "form": "D,L,L,D,L", "won": 2, "draw": 2, "lost": 6, "points": 8, "goalsFor": 8, "goalsAgainst": 17, "goalDifference": -9},
    {"position": 18, "team": {"id": 5890, "name": "Hellas Verona", "shortName": "Verona", "tla": "VER"}, "playedGames": 10, "form": "L,L,W,L,L", "won": 2, "draw": 1, "lost": 7, "points": 7, "goalsFor": 8, "goalsAgainst": 19, "goalDifference": -11},
    {"position": 19, "team": {"id": 471, "name": "Sassuolo", "shortName": "Sassuolo", "tla": "SAS"}, "playedGames": 10, "form": "L,D,L,L,D", "won": 1, "draw": 3, "lost": 6, "points": 6, "goalsFor": 7, "goalsAgainst": 18, "goalDifference": -11},
    {"position": 20, "team": {"id": 487, "name": "Salernitana", "shortName": "Salernitana", "tla": "SAL"}, "playedGames": 10, "form": "L,L,L,D,L", "won": 1, "draw": 1, "lost": 8, "points": 4, "goalsFor": 6, "goalsAgainst": 22, "goalDifference": -16},
]

LAST_RESULTS = [
    {
        "id": 1,
        "utcDate": "2024-11-02T19:45:00Z",
        "status": "FINISHED",
        "matchday": 10,
        "homeTeam": {"id": 98, "name": "Milan", "shortName": "Milan", "tla": "MIL"},
        "awayTeam": {"id": 505, "name": "Inter", "shortName": "Inter", "tla": "INT"},
        "score": {"winner": "AWAY_TEAM", "fullTime": {"home": 1, "away": 2}, "halfTime": {"home": 1, "away": 1}},
    },
    {
        "id": 2,
        "utcDate": "2024-11-02T17:00:00Z",
        "status": "FINISHED",
        "matchday": 10,
        "homeTeam": {"id": 109, "name": "Juventus", "shortName": "Juventus", "tla": "JUV"},
        "awayTeam": {"id": 113, "name": "Napoli", "shortName": "Napoli", "tla": "NAP"},
        "score": {"winner": "DRAW", "fullTime": {"home": 0, "away": 0}, "halfTime": {"home": 0, "away": 0}},
    },
    {
        "id": 3,
        "utcDate": "2024-11-01T19:45:00Z",
        "status": "FINISHED",
        "matchday": 10,
        "homeTeam": {"id": 102, "name": "Atalanta", "shortName": "Atalanta", "tla": "ATA"},
        "awayTeam": {"id": 100, "name": "Roma", "shortName": "Roma", "tla": "ROM"},
        "score": {"winner": "HOME_TEAM", "fullTime": {"home": 3, "away": 1}, "halfTime": {"home": 2, "away": 0}},
    },
    {
        "id": 4,
        "utcDate": "2024-11-01T17:00:00Z",
        "status": "FINISHED",
        "matchday": 10,
        "homeTeam": {"id": 103, "name": "Lazio", "shortName": "Lazio", "tla": "LAZ"},
        "awayTeam": {"id": 99, "name": "Fiorentina", "shortName": "Fiorentina", "tla": "FIO"},
        "score": {"winner": "DRAW", "fullTime": {"home": 2, "away": 2}, "halfTime": {"home": 1, "away": 1}},
    },
    {
        "id": 5,
        "utcDate": "2024-10-31T19:45:00Z",
        "status": "FINISHED",
        "matchday": 10,
        "homeTeam": {"id": 586, "name": "Bologna", "shortName": "Bologna", "tla": "BOL"},
        "awayTeam": {"id": 445, "name": "Cagliari", "shortName": "Cagliari", "tla": "CAG"},
        "score": {"winner": "HOME_TEAM", "fullTime": {"home": 2, "away": 0}, "halfTime": {"home": 1, "away": 0}},
    },
]


def get_competition():
    return COMPETITION


def get_standings():
    return STANDINGS


def get_last_results():
    return LAST_RESULTS
