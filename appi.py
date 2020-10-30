from fastapi import FastAPI
import json 
import uvicorn
import random

#Init API
app = FastAPI()

#Import the file products
from products import products

#Route
@app.get('/products')
def leer_ruta():
    return {'Products Available': products}

if __name__ == '_main_':
    uvicorn.run(app, host="127.0.0.1",port='8000')



