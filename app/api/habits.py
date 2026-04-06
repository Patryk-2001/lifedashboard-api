from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app.core.database import get_db
from app.schemas.habit import HabitCreate, HabitResponse
from app.services.habits import (
    create_habit, get_habits, get_habits_by_date,
    update_habit, delete_habit
)

router = APIRouter(prefix="/habits", tags=["Habits"])

@router.post("/", response_model=HabitResponse)
def add_habit(habit: HabitCreate, db: Session = Depends(get_db)):
    return create_habit(db, habit)

@router.get("/", response_model=list[HabitResponse])
def list_habits(db: Session = Depends(get_db)):
    return get_habits(db)

@router.get("/today", response_model=list[HabitResponse])
def habits_today(db: Session = Depends(get_db)):
    return get_habits_by_date(db, date.today())

@router.patch("/{habit_id}", response_model=HabitResponse)
def toggle_habit(habit_id: int, completado: bool, db: Session = Depends(get_db)):
    habit = update_habit(db, habit_id, completado)
    if not habit:
        raise HTTPException(status_code=404, detail="Hábito no encontrado")
    return habit

@router.delete("/{habit_id}")
def remove_habit(habit_id: int, db: Session = Depends(get_db)):
    habit = delete_habit(db, habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Hábito no encontrado")
    return {"mensaje": "Hábito eliminado correctamente"}