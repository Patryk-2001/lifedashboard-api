from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    completado = Column(Boolean, default=False)
    fecha = Column(Date, nullable=False)
    notas = Column(String, nullable=True)
    creado_en = Column(DateTime, server_default=func.now())