from fastapi import FastAPI

from database import create_db_and_tables
from endpoints.team_endpoints import team_route
from endpoints.hero_endpoints import hero_route

app = FastAPI()

app.include_router(team_route)

app.include_router(hero_route)


# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()
