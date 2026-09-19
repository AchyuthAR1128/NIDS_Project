import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "database", "db.db")


def createDabase():
    global conn, cursor

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()


def InsertData(name, email, password, mobile):

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, email, password, mobile) VALUES (?, ?, ?, ?)",
        (name, email, password, mobile)
    )

    conn.commit()
    conn.close()

    print("Inserted Data")


def read_cred(email, password):

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT username, email, password, mobile "
        "FROM users WHERE email = ? AND password = ?",
        (email, password)
    )

    fetch = cursor.fetchone()
    conn.close()

    print(fetch)

    return fetch


createDabase()