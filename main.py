from fastapi import FastAPI
from DB import db

app = FastAPI()


# Run once when the app starts
@app.on_event("startup")
def startup_event():
    db.init_db()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/register/")
async def register_user(username: str, password: str):
    print(f"Registering user: {username}")
    db.add_user(username, password)
    return {"status": "User registered successfully"}