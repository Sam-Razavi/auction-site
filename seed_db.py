import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

DB_PATH = Path("instance/auction.db")


def seed():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Clear old data
    cur.execute("DELETE FROM bids")
    cur.execute("DELETE FROM reactions")
    cur.execute("DELETE FROM auctions")

    now = datetime.now()

    auctions = [
        (
            "Vintage Camera",
            "Electronics",
            "A classic 35mm film camera in good working condition.",
            100,
            (now + timedelta(days=3)).strftime("%Y-%m-%d %H:%M"),
            "camera.jpg",
        ),
        (
            "Handmade Wooden Chair",
            "Furniture",
            "Handcrafted wooden chair made from oak.",
            250,
            (now + timedelta(days=7)).strftime("%Y-%m-%d %H:%M"),
            "chair.jpg",
        ),
        (
            "Gaming Laptop",
            "Electronics",
            "High-performance gaming laptop with RTX graphics.",
            800,
            (now + timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
            "laptop.jpg",
        ),
        (
            "Abstract Painting",
            "Art",
            "Colorful abstract painting by a local artist.",
            300,
            (now + timedelta(days=10)).strftime("%Y-%m-%d %H:%M"),
            "painting.jpg",
        ),
        (
            "Road Bike",
            "Sports",
            "Lightweight road bike, barely used.",
            600,
            (now - timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
            "bike.jpg",
        ),
        (
            "Coffee Grinder",
            "Kitchen",
            "Electric coffee grinder with multiple settings.",
            50,
            (now + timedelta(days=5)).strftime("%Y-%m-%d %H:%M"),
            "grinder.jpg",
        ),
        (
            "Desk Lamp",
            "Home",
            "Minimalist LED desk lamp.",
            40,
            (now + timedelta(days=2)).strftime("%Y-%m-%d %H:%M"),
            "lamp.jpg",
        ),
        (
            "Vinyl Record Collection",
            "Music",
            "Collection of classic rock vinyl records.",
            120,
            (now - timedelta(days=2)).strftime("%Y-%m-%d %H:%M"),
            "vinyl.jpg",
        ),
    ]

    cur.executemany(
        """
        INSERT INTO auctions (title, category, description, starting_bid, end_datetime, image_filename)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        auctions,
    )

    bids = [
        (1, "alice@example.com", 120, now.strftime("%Y-%m-%d %H:%M")),
        (1, "bob@example.com", 150, now.strftime("%Y-%m-%d %H:%M")),
        (2, "carol@example.com", 260, now.strftime("%Y-%m-%d %H:%M")),
        (3, "dan@example.com", 900, now.strftime("%Y-%m-%d %H:%M")),
        (3, "erin@example.com", 950, now.strftime("%Y-%m-%d %H:%M")),
        (6, "frank@example.com", 60, now.strftime("%Y-%m-%d %H:%M")),
    ]

    cur.executemany(
        """
        INSERT INTO bids (auction_id, bidder_email, bid_amount, bid_datetime)
        VALUES (?, ?, ?, ?)
        """,
        bids,
    )

    conn.commit()
    conn.close()
    print("Database seeded with mock data (including images).")


if __name__ == "__main__":
    seed()
