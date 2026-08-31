from sqlalchemy.orm import Session
from app.models.bill import Bill
from app.schemas.bill import BillCreate
from sqlalchemy import func

def create_bill(db: Session, bill: BillCreate):
    db_bill = Bill(**bill.model_dump())
    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)
    return db_bill

def get_bills(db: Session):
    return db.query(Bill).order_by(Bill.fecha.desc()).all()

def get_bills_by_date(db: Session, fecha):
    return db.query(Bill).filter(Bill.fecha == fecha).all()

def update_bill(db: Session, bill_id: int, completado: bool):
    bill = db.query(Bill).filter(Bill.id == bill_id).first()
    if bill:
        bill.completado = completado
        db.commit()
        db.refresh(bill)
    return bill

def delete_bill(db: Session, bill_id: int):
    bill = db.query(Bill).filter(Bill.id == bill_id).first()
    if bill:
        db.delete(bill)
        db.commit()
    return bill

def get_summary(db: Session):
    results = db.query(
        Bill.categoria,
        func.sum(Bill.cantidad).label("total"),
        func.count(Bill.id).label("num_gastos")
    ).group_by(Bill.categoria).all()

    return [
        {
            "categoria": r.categoria,
            "total": round(r.total, 2),
            "num_gastos": r.num_gastos
        }
        for r in results
    ]