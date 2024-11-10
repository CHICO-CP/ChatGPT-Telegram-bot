import sqlite3
import os

def connect_db():
    os.makedirs('data', exist_ok=True)
    return sqlite3.connect('data/long_carve.db')

def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            query TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def store_query(user_id, query, response):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO user_queries (user_id, query, response)
        VALUES (?, ?, ?)
    ''', (user_id, query, response))
    conn.commit()
    conn.close()
