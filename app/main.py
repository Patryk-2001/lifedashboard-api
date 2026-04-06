from fastapi import FastAPI
from app.core.config import settings
from app.api.weather import router as weather_router
from app.api.finance import router as finance_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)

app.include_router(weather_router)
app.include_router(finance_router)

@app.get("/health")
def health():
    return {"status": "ok", "version": settings.app_version}