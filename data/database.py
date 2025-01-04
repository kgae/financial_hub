# data/database.py

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / 'financial_hub.db'

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            balance REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (account_id) REFERENCES accounts (id)
        )
    ''')

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS investments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL, -- 'crypto', 'stocks', 'etf'
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
        """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS debts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            total_amount REAL NOT NULL,
            remaining_amount REAL NOT NULL,
            due_date TEXT NOT NULL,
            interest_rate REAL NOT NULL
        )
        """)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
    print('Database initialized.')
