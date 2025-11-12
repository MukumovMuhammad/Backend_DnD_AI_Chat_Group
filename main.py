from fastapi import FastAPI
from DB import db
import secrets

app = FastAPI()


def generate_token():
    # Generates a random URL-safe text string, suitable for use in tokens
    return secrets.token_urlsafe(32) # 32 bytes of randomness

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

    token = generate_token()
    print(f"Users token! {token}")
    db.add_user(username, password,token)
    return {"status": "User registered successfully", "token" : token}




@app.post("/login/")
async def login_user(username: str, password: str):
    user = db.get_user(username)
    if user and user["password"] == password:
        return {"status": "Login successful"}
    return {"status": "Invalid username or password"}


######### End of User Registration and Login #########