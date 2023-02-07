from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app =  FastAPI()

@app.get("/")
def root():
    return{"msg":"welcom to root page"}

