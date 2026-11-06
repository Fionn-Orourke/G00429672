from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints
Pattern = Annotated[str, StringConstraints(pattern=r"ST-\d{4}$")]
class EquipmentCreate(BaseModel):
    equipment_id:int
    student_id:Pattern
    description:Annotated[str,StringConstraints(min_length=5, max_length=100)]
    priority:int=Field(gt=0, lt=6, le=5)
    status:str=Field(default="OPEN")

class EquipmentRead(BaseModel):
    equipment_id:int
    student_id:str
    description:str
    priority:int
    status:str
