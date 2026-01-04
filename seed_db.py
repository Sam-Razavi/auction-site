import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path("instance/auction.db")

def seed():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO auctions (title, category, description, starting_bid, end_datetime)
        VALUES (?, ?, ?, ?, ?)
        """,
        ("Vintage Camera", "Electronics", "Old camera in good condition.", 100, "2026-01-10 18:00")
    )

    cur.execute(
        """
        INSERT INTO auctions (title, category, description, starting_bid, end_datetime)
        VALUES (?, ?, ?, ?, ?)
        """,
        ("Coffee Table", "Home", "Wooden coffee table. Some small scratches.", 200, "2026-01-08 12:00")
    )

    conn.commit()
    conn.close()
    print("Seeded auctions!")

if __name__ == "__main__":
    seed()
