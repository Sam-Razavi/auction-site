import sqlite3
from pathlib import Path

DB_PATH = Path("instance/auction.db")

def add_bids():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # bids for auction 1
    cur.execute(
        "INSERT INTO bids (auction_id, bidder_email, bid_amount, bid_datetime) VALUES (?, ?, ?, ?)",
        (1, "alice@example.com", 120, "2026-01-04 16:10")
    )
    cur.execute(
        "INSERT INTO bids (auction_id, bidder_email, bid_amount, bid_datetime) VALUES (?, ?, ?, ?)",
        (1, "bob@example.com", 150, "2026-01-04 16:12")
    )
    cur.execute(
        "INSERT INTO bids (auction_id, bidder_email, bid_amount, bid_datetime) VALUES (?, ?, ?, ?)",
        (1, "carol@example.com", 140, "2026-01-04 16:11")
    )

    conn.commit()
    conn.close()
    print("Added test bids!")

if __name__ == "__main__":
    add_bids()
