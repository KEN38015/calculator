from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database import Base, engine
from .routers import api_keys, items, pages

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HTMX + FastAPI Starter")

app.mount("/static", StaticFiles(directory=str(Path(__file__).parent / "static")), name="static")

app.include_router(pages.router)
app.include_router(api_keys.router)
app.include_router(items.router)
