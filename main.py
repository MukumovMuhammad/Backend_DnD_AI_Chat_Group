from fastapi import FastAPI
from DB import db

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

