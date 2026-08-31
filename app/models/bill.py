from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    categoria = Column(String, nullable=False)
    fecha = Column(Date, nullable=False)
    notas = Column(String, nullable=True)
    creado_en = Column(DateTime, server_default=func.now())