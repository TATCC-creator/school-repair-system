import sqlite3

def login(username,password):

    conn = sqlite3.connect("repairs.db")
    cursor = conn.cursor()

    cursor.execute(
    "SELECT role FROM users WHERE username=? AND password=?",
    (username,password)
    )

    result = cursor.fetchone()
    conn.close()

    return result