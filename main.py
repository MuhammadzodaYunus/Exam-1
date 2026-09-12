from fastapi import FastAPI, Depends, HTTPException
from models import Product
from schemas import ProductIn, ProductOut, ProductPatch
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy import select

app = FastAPI()


@app.post("/product", response_model=ProductOut, status_code=201)
def create_product(data: ProductIn, db: Session = Depends(get_db)):
    product = Product(title=data.title, price=data.price, quantity=data.quantity)

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


@app.get("/product", response_model=list[ProductOut])
def get_all_products(db: Session = Depends(get_db)):
    smtm = select(Product)

    products = db.execute(smtm).scalars().all()

    return products


@app.get("/product/{product_id}", response_model=ProductOut)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=404, detail="Product with this id did not found"
        )

    return product


@app.put("/product/{product_id}", response_model=ProductOut)
def put_product_by_id(product_id: int, data: ProductIn, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=404, detail="Product with this id did not found"
        )

    product.title = data.title
    product.price = data.price
    product.quantity = data.quantity

    db.commit()
    db.refresh(product)

    return product


@app.patch("/product/{product_id}", response_model=ProductOut)
def patch_product(product_id: int, data: ProductPatch, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=404, detail="Product with this id did not found"
        )

    new_data = data.model_dump(exclude_unset=True)

    for key, value in new_data.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


@app.delete("/product/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=404, detail="Product with this id did not found"
        )

    db.delete(product)
    db.commit()
