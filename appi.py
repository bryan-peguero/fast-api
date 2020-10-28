from fastapi import FastAPI 
import uvicorn
import json
import random

#Init API
app = FastAPI()

#Route
@app.get('/')
def leer_ruta(name: str = "Default", lname: str = "Default", tl: int = "Default", country: str = "Default", sex: str = "Default"):
    return {"id": random.randint(0, 1000),
            "Name": name,
            "Last Name": lname,
            "Telephone": tl,
            "Country": country,
            "Genre": sex
            }

if __name__ == '_main_':
    uvicorn.run(app, host='127.0.0.1', port='5500')



