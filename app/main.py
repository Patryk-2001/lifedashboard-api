from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.api.weather import router as weather_router
from app.api.finance import router as finance_router
from app.api.habits import router as habits_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)

app.include_router(weather_router)
app.include_router(finance_router)
app.include_router(habits_router)

@app.get("/health")
def health():
    return {"status": "ok", "version": settings.app_version}