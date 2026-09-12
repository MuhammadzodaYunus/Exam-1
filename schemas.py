from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

class ProductIn(BaseModel):

    title: str = Field(max_length=55)
    price: Decimal = Field(max_digits=10, decimal_places=2, gt=0)
    quantity: int = Field(gt=0)

class ProductOut(BaseModel):

    id: int
    title: str
    price: Decimal
    quantity: int

    model_config = ConfigDict(from_attributes=True)


class ProductPatch(BaseModel):

    title: str | None = Field(default=None, max_length=55)
    price: Decimal | None = Field(default=None, gt=0)
    quantity: int | None = Field(default=None, gt=0)
    