import sqlite3
from pathlib import Path

DB_PATH = Path("instance/auction.db")
SCHEMA_PATH = Path("app/schema.sql")

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.close()
    print("Database created:", DB_PATH)

if __name__ == "__main__":
    init_db()
