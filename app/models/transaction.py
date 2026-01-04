from datetime import datetime

from sqlalchemy import (
    TIMESTAMP,
    CheckConstraint,
    ForeignKey,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id: Mapped[int] = mapped_column(primary_key=True)

    family_id: Mapped[int] = mapped_column(
        ForeignKey("families.family_id"), nullable=False
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.category_id"), nullable=False
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.account_id"), nullable=False
    )

    kind: Mapped[str] = mapped_column(
        String(10), nullable=False
    )  # 'expense' | 'income'

    amount: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)

    transaction_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)

    __table_args__ = (
        CheckConstraint(
            "kind IN ('expense', 'income')",
            name="ck_transactions_kind",
        ),
        CheckConstraint(
            "amount > 0",
            name="ck_transactions_amount_positive",
        ),
    )
    user = relationship("User")
    category = relationship("Category")
    account = relationship("Account")
    family = relationship("Family")
