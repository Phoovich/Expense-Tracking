from datetime import datetime
from pydantic import BaseModel, ConfigDict


class FamilyCreate(BaseModel):
    family_name: str


class FamilyOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    family_id: int
    family_name: str
    created_at: datetime
