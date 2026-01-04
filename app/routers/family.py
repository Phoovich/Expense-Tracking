from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.family import Family
from app.schemas.family import FamilyCreate, FamilyOut

router = APIRouter(prefix="/families", tags=["Families"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=FamilyOut)
def create_family(
    data: FamilyCreate,
    db: Session = Depends(get_db),
):
    family = Family(**data.model_dump())
    db.add(family)
    db.commit()
    db.refresh(family)
    return family
