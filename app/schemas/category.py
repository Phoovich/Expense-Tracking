from pydantic import BaseModel, ConfigDict


class CategoryCreate(BaseModel):
    family_id: int
    cat_name: str
    kind: str  # 'expense' | 'income'


class CategoryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    category_id: int
    family_id: int
    cat_name: str
    kind: str
