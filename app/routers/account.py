from typing import Literal

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.account import Account
from app.schemas.account import AccountCreate, AccountOut

router = APIRouter(prefix="/accounts", tags=["Accounts"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AccountOut)
def create_account(
    data: AccountCreate,
    db: Session = Depends(get_db),
):
    account = Account(**data.model_dump())
    db.add(account)
    db.commit()
    db.refresh(account)
    return account


@router.get("/", response_model=list[AccountOut])
def list_accounts(
    family_id: int = Query(..., description="Family ID"),
    type: Literal["cash", "bank", "credit", "ewallet"] | None = Query(
        None, description="Filter by account type"
    ),
    db: Session = Depends(get_db),
):
    q = db.query(Account).filter(Account.family_id == family_id)

    if type is not None:
        q = q.filter(Account.type == type)

    return q.order_by(Account.account_id.asc()).all()
