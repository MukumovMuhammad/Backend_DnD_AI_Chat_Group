import sqlite3
from DB.db import get_db_connection


def add_friends_chat(user1, user2, messages='[]'):
    conn = get_db_connection()
    conn.execute("""
        INSERT INTO friends_chat (user1, user2, messages)
        VALUES (?, ?, ?)
    """, (user1, user2, messages))
    conn.commit()
    conn.close()

def get_friends_chat(user1, user2):
    conn = get_db_connection()
    chat = conn.execute("""
        SELECT * FROM friends_chat WHERE (user1 = ? AND user2 = ?) OR (user1 = ? AND user2 = ?)
    """, (user1, user2, user2, user1)).fetchone()
    conn.close()
    return chat

# It just updates the list of chat friends in the user's profile
def update_user_chat_friends(username, chat_friends):
    conn = get_db_connection()
    conn.execute("""
        UPDATE users SET chat_friends = ? WHERE username = ?
    """, (chat_friends, username))
    conn.commit()
    conn.close()

# Updates the messages in a specific friends chat
def update_friends_chat_messages(chat_id, messages):
    conn = get_db_connection()
    conn.execute("""
        UPDATE friends_chat SET messages = ? WHERE id = ?
    """, (messages, chat_id))
    conn.commit()
    conn.close()
