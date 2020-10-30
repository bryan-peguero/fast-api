from fastapi import FastAPI
from pydantic import BaseModel
import json
import uvicorn
import random

class Product(BaseModel):
    name: str
    price: int
    description: str
    in_stock: int

#Init API
app = FastAPI()

#Import the file products
from products import products

#Route
@app.get('/products')
def read_route():
    return {'Products Available': products}

#Search a product
@app.get('/products/{product_name}')
def get_Product(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    return {'The product was founded': productFound}

#POST a product
@app.post('/products/{product_name}')
def post_Product(product: Product):
    products.append(product.dict())
    return {'Product added succesfully': products}

if __name__ == '_main_':
    uvicorn.run(app, host="127.0.0.1",port='8000')



