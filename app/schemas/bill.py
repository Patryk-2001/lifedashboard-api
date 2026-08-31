from pydantic import BaseModel
from datetime import date, datetime

class BillCreate(BaseModel):
    descripcion: str
    cantidad: float
    categoria: str
    fecha: date
    notas: str | None = None

class BillResponse(BaseModel):
    id: int
    descripcion: str
    cantidad: float
    categoria: str
    fecha: date
    notas: str | None
    creado_en: datetime

    model_config = {"from_attributes": True}