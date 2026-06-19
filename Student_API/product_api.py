from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Product Model
class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

# In-memory storage
products = []

# GET All Products
@app.get("/products", response_model=List[Product])
def get_products():
    return products

# POST Product
@app.post("/products", status_code=status.HTTP_201_CREATED)
def add_product(product: Product):
    products.append(product)
    return {
        "message": "Product added successfully",
        "product": product
    }

# PUT Product
@app.put("/products/{id}")
def update_product(id: int, updated_product: Product):

    for index, product in enumerate(products):

        if product.id == id:
            products[index] = updated_product

            return {
                "message": "Product updated successfully",
                "product": updated_product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )

# DELETE Product
@app.delete("/products/{id}")
def delete_product(id: int):

    for index, product in enumerate(products):

        if product.id == id:
            deleted_product = products.pop(index)

            return {
                "message": "Product deleted successfully",
                "product": deleted_product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )