
import sqlite3
from DB.db import get_db_connection


def add_chat_group(group_name, members='[]', messages='[]'):
    conn = get_db_connection()
    conn.execute("""
        INSERT INTO chat_group (group_name, members, messages)
        VALUES (?, ?, ?)
    """, (group_name, members, messages))
    conn.commit()
    conn.close()

def get_chat_group(group_name):
    conn = get_db_connection()
    group = conn.execute("""
        SELECT * FROM chat_group WHERE group_name = ?
    """, (group_name,)).fetchone()
    conn.close()
    return group

def update_chat_group_messages(group_id, messages):
    conn = get_db_connection()
    conn.execute("""
        UPDATE chat_group SET messages = ? WHERE id = ?
    """, (messages, group_id))
    conn.commit()
    conn.close()

