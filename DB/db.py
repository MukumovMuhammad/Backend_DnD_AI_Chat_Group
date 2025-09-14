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
            password TEXT NOT NULL
        );

        -- Table for mutual, confirmed friendships
        CREATE TABLE IF NOT EXISTS friendships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            friend_id INTEGER NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (friend_id) REFERENCES users (id),
            UNIQUE (user_id, friend_id)
        );

        -- Table for pending friend requests
        CREATE TABLE IF NOT EXISTS friend_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER NOT NULL,
            status TEXT DEFAULT 'pending',
            created_at TEXT NOT NULL,
            FOREIGN KEY (sender_id) REFERENCES users (id),
            FOREIGN KEY (receiver_id) REFERENCES users (id)
        );

        -- Table for one-on-one chats between friends
        CREATE TABLE IF NOT EXISTS friends_chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user1_id INTEGER NOT NULL,
            user2_id INTEGER NOT NULL,
            messages TEXT DEFAULT '[]',
            FOREIGN KEY (user1_id) REFERENCES users (id),
            FOREIGN KEY (user2_id) REFERENCES users (id)
        );

        -- Table for group chats
        CREATE TABLE IF NOT EXISTS game_groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT NOT NULL,
            members TEXT DEFAULT '[]',
            messages TEXT DEFAULT '[]'
        );
    """)
    print("Database initialized.")
    conn.commit()
    conn.close()




def add_user(username, password):
    #Adds a new user to the database.
    print(f"Adding user: {username}")
    conn = get_db_connection()
    conn.execute("""
        INSERT INTO users (username, password)
        VALUES (?, ?)
    """, (username, password))
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
