from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import mock_data

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Serie A Stats")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    competition = mock_data.get_competition()
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "competition": competition},
    )


@app.get("/table", response_class=HTMLResponse)
def table(request: Request):
    standings = mock_data.get_standings()
    return templates.TemplateResponse(
        "table.html",
        {"request": request, "standings": standings},
    )


@app.get("/last_results", response_class=HTMLResponse)
def last_results(request: Request):
    matches = mock_data.get_last_results()
    return templates.TemplateResponse(
        "last_results.html",
        {"request": request, "matches": matches},
    )
