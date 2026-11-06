from sqlalchemy  import Integer, String, Float, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.database import Base

class Base(DeclarativeBase):
    pass

class EquipmentDB(Base):
    __tablename__ = "requests"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    equipment_id:Mapped[int] = mapped_column(Integer, nullable=False)
    student_id:Mapped[str]= mapped_column(String(255), unique=True, index=True, nullable=False)
    description:Mapped[str]= mapped_column(String(255), unique=False, index = True, nullable=True)
    priority:Mapped[int]=mapped_column(Integer, nullable=False, unique=False)
    status:Mapped[str]=mapped_column(Integer, nullable=False, unique=False)

