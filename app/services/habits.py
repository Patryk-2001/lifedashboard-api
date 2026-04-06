from sqlalchemy.orm import Session
from app.models.habit import Habit
from app.schemas.habit import HabitCreate

def create_habit(db: Session, habit: HabitCreate):
    db_habit = Habit(**habit.model_dump())
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

def get_habits(db: Session):
    return db.query(Habit).order_by(Habit.fecha.desc()).all()

def get_habits_by_date(db: Session, fecha):
    return db.query(Habit).filter(Habit.fecha == fecha).all()

def update_habit(db: Session, habit_id: int, completado: bool):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if habit:
        habit.completado = completado
        db.commit()
        db.refresh(habit)
    return habit

def delete_habit(db: Session, habit_id: int):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if habit:
        db.delete(habit)
        db.commit()
    return habit