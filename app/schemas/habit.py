from pydantic import BaseModel
from datetime import date, datetime

class HabitCreate(BaseModel):
    nombre: str
    completado: bool = False
    fecha: date
    notas: str | None = None

class HabitResponse(BaseModel):
    id: int
    nombre: str
    completado: bool
    fecha: date
    notas: str | None
    creado_en: datetime

    model_config = {"from_attributes": True}