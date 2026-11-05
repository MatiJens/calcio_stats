from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator

from app import api

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Serie A Stats", version="0.1.0")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    competition = api.get_competition()
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "competition": competition},
    )


@app.get("/table", response_class=HTMLResponse)
def table(request: Request):
    standings = api.get_standings()
    return templates.TemplateResponse(
        "table.html",
        {"request": request, "standings": standings},
    )


@app.get("/last_results", response_class=HTMLResponse)
def last_results(request: Request):
    matches = api.get_last_results()
    return templates.TemplateResponse(
        "last_results.html",
        {"request": request, "matches": matches},
    )
