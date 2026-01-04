from typing import Literal

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.category import Category
from app.schemas.category import CategoryOut

router = APIRouter(prefix="/categories", tags=["Categories"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[CategoryOut])
def list_categories(
    family_id: int = Query(..., description="Family ID"),
    kind: Literal["expense", "income"] | None = Query(
        None, description="Filter by expense or income"
    ),
    db: Session = Depends(get_db),
):
    q = db.query(Category).filter(Category.family_id == family_id)

    if kind is not None:
        q = q.filter(Category.kind == kind)

    return q.order_by(Category.category_id.asc()).all()
