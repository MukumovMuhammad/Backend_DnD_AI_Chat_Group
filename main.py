from fastapi import FastAPI
from DB import db

app = FastAPI()


# Run once when the app starts
@app.on_event("startup")
def startup_event():
    db.init_db()

@app.get("/")
async def read_root():
    return {"The server is running": "Welcome to DnD Chat Group!, This is a test server."}

######## User Registration and Login ########
@app.post("/register/")
async def register_user(username: str, password: str):
    print(f"Registering user: {username}")
    db.add_user(username, password)
    return {"status": "User registered successfully"}



@app.post("/login/")
async def login_user(username: str, password: str):
    user = db.get_user(username)
    if user and user["password"] == password:
        return {"status": "Login successful"}
    return {"status": "Invalid username or password"}


######### End of User Registration and Login #########