import sqlite3

def create_db():

    conn = sqlite3.connect("repairs.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS repairs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT,
        category TEXT,
        location TEXT,
        room TEXT,
        reporter TEXT,
        repair_time TEXT,
        description TEXT,
        photo TEXT,
        status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    conn.commit()
    conn.close()

create_db()