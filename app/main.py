from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)

@app.get("/health")
def health():
    return {"status": "ok", "version": settings.app_version}