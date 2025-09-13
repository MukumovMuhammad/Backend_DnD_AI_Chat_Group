import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



def init_db():
    print("Initializing database...")
    conn = get_db_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            friends TEXT DEFAULT '[]',
            chat_friends TEXT DEFAULT '[]',
            chat_ai_games TEXT DEFAULT '[]'
        );

        CREATE TABLE IF NOT EXISTS friends_chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user1 TEXT NOT NULL,
            user2 TEXT NOT NULL,
            messages TEXT DEFAULT '[]'
        );

        CREATE TABLE IF NOT EXISTS chat_group (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT NOT NULL,
            members TEXT DEFAULT '[]',
            messages TEXT DEFAULT '[]'
        );
    """)
    print("Database initialized.")
    conn.commit()
    conn.close()


def add_user(username, password, friends='[]', chat_friends='[]', chat_ai_games='[]'):
    print(f"Adding user: {username}")
    conn = get_db_connection()
    conn.execute("""
        INSERT INTO users (username, password, friends, chat_friends, chat_ai_games)
        VALUES (?, ?, ?, ?, ?)
    """, (username, password, friends, chat_friends, chat_ai_games))
    conn.commit()
    print(f"User {username} added successfully.")
    conn.close()


def get_user(username):
    conn = get_db_connection()
    user = conn.execute("""
        SELECT * FROM users WHERE username = ?
    """, (username,)).fetchone()
    conn.close()
    return user


def update_user_friends(username, friends):
    conn = get_db_connection()
    conn.execute("""
        UPDATE users SET friends = ? WHERE username = ?
    """, (friends, username))
    conn.commit()
    conn.close()


