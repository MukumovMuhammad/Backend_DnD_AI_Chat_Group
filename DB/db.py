import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



def init_db():
    """Initializes the database with all necessary tables."""
    print("Initializing database...")
    conn = get_db_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            token TEXT
        );

    """)
    print("Database initialized.")
    conn.commit()
    conn.close()




def add_user(username, password, token):
    #Adds a new user to the database.
    print(f"Adding user: {username}")
    conn = get_db_connection()
    conn.execute("""
        INSERT INTO users (username, password, token)
        VALUES (?, ?, ?)
    """, (username, password, token))
    conn.commit()
    print(f"User {username} added successfully.")
    conn.close()


# This function now has no purpose, and kinda not usuful but later It will be modified to add more user details. (I hope so...)
def get_user(username):
    #Retrieves a user's record by username.
    conn = get_db_connection()
    user = conn.execute("""
        SELECT * FROM users WHERE username = ?
    """, (username,)).fetchone()
    conn.close()
    return user
