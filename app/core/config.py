from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "LifeDashboard API"
    app_version: str = "0.1.0"
    debug: bool = True

    openweather_api_key: str = ""
    openweather_city: str = "Madrid"

    database_url: str = ""

    class Config:
        env_file = ".env"

settings = Settings()