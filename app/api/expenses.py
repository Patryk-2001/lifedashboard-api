from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app.core.database import get_db
from app.schemas.bill import BillCreate, BillResponse
from app.services.expenses import (
    create_bill, get_bills, get_bills_by_date,
    update_bill, delete_bill, get_summary
)

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/", response_model=BillResponse)
def add_bill(bill: BillCreate, db: Session = Depends(get_db)):
    return create_bill(db, bill)

@router.get("/", response_model=list[BillResponse])
def list_bills(db: Session = Depends(get_db)):
    return get_bills(db)

@router.get("/today", response_model=list[BillResponse])
def bills_today(db: Session = Depends(get_db)):
    return get_bills_by_date(db, date.today())

@router.patch("/{bill_id}", response_model=BillResponse)
def toggle_bill(bill_id: int, completado: bool, db: Session = Depends(get_db)):
    bill = update_bill(db, bill_id, completado)
    if not bill:
        raise HTTPException(status_code=404, detail="Hábito no encontrado")
    return bill

@router.delete("/{bill_id}")
def remove_bill(bill_id: int, db: Session = Depends(get_db)):
    bill = delete_bill(db, bill_id)
    if not bill:
        raise HTTPException(status_code=404, detail="Hábito no encontrado")
    return {"mensaje": "Hábito eliminado correctamente"}

@router.get("/summary")
def bills_summary(db: Session = Depends(get_db)):
    return get_summary(db)