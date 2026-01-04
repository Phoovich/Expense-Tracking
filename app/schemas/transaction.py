from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TransactionCreate(BaseModel):
    family_id: int
    user_id: int
    category_id: int
    account_id: int
    kind: str  # 'expense' | 'income'
    amount: float
    transaction_time: datetime
    description: str | None = None


class TransactionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    transaction_id: int
    family_id: int
    user_id: int
    category_id: int
    account_id: int
    kind: str
    amount: float
    transaction_time: datetime
    description: str | None
    created_at: datetime
