from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, CheckConstraint, Numeric
from decimal import Decimal


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(55), nullable=False)
    price: Mapped[Decimal] = mapped_column(
        Numeric(precision=10, scale=2), nullable=False
    )
    quantity: Mapped[int] = mapped_column()

    __table_args__ = (CheckConstraint("price > 0"), CheckConstraint("quantity > 0"))

    def __repr__(self):
        return self.title
