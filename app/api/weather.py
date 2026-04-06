from fastapi import APIRouter, HTTPException
from app.services.weather import get_current_weather

router = APIRouter(prefix="/weather", tags=["Weather"])

@router.get("/now")
async def weather_now():
    try:
        return await get_current_weather()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))