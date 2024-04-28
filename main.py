from typing import Optional
from fastapi import FastAPI
from services.dosomething import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/do")
def read_item():
    return do()