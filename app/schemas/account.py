from datetime import datetime
from pydantic import BaseModel, ConfigDict


class AccountCreate(BaseModel):
    family_id: int
    name: str
    type: str  # 'cash' | 'bank' | 'credit' | 'ewallet'


class AccountOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    account_id: int
    family_id: int
    name: str
    type: str
    created_at: datetime
