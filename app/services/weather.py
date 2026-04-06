import httpx
from app.core.config import settings

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

async def get_current_weather():
    params = {
        "q": settings.openweather_city,
        "appid": settings.openweather_api_key,
        "units": "metric",
        "lang": "es"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(OPENWEATHER_URL, params=params)
        response.raise_for_status()
        data = response.json()

    return {
        "ciudad": data["name"],
        "temperatura": data["main"]["temp"],
        "sensacion_termica": data["main"]["feels_like"],
        "humedad": data["main"]["humidity"],
        "descripcion": data["weather"][0]["description"],
        "viento_kmh": round(data["wind"]["speed"] * 3.6, 1)
    }