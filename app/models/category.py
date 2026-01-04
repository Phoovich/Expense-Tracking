from sqlalchemy import CheckConstraint, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(primary_key=True)

    family_id: Mapped[int] = mapped_column(
        ForeignKey("families.family_id"),
        nullable=False,
    )

    cat_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    kind: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    family = relationship("Family")

    __table_args__ = (
        CheckConstraint(
            "kind IN ('expense', 'income')",
            name="ck_categories_kind",
        ),
    )
