from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.models import EquipmentDB
from app.schemas import EquipmentCreate, EquipmentRead
Base.metadata.create_all(bind = engine)

app = FastAPI(title="CICD2 Exam")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post(
    "/api/requests",
    response_model= EquipmentRead,
    status_code=status.HTTP_201_CREATED,
)
def create_equipment(equipment_in:EquipmentCreate, db:Session= Depends(get_db)):
    db_equipment = EquipmentDB(**equipment_in.model_dump())
    db.add(db_equipment)
    try:
        db.commit()
        db.refresh(db_equipment)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="equipment with this unique detail already exists",)
    return db_equipment

@app.get("/api/requests", response_model=list[EquipmentRead])
def get_equipment(db:Session=Depends(get_db)):
    stmt=select(EquipmentDB).order_by(EquipmentDB.id)
    return db.execute(stmt).scalars().all()

