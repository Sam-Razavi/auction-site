from datetime import datetime
from app.db import get_db


class AuctionRepository:
    # -------- Auctions --------

    def get_all(self):
        db = get_db()
        rows = db.execute(
            """
            SELECT id, title, category, description, starting_bid, end_datetime
            FROM auctions
            ORDER BY end_datetime ASC
            """
        ).fetchall()
        return rows

    def search(self, keyword):
        db = get_db()
        kw = f"%{keyword}%"
        rows = db.execute(
            """
            SELECT id, title, category, description, starting_bid, end_datetime
            FROM auctions
            WHERE title LIKE ? OR description LIKE ?
            ORDER BY end_datetime ASC
            """,
            (kw, kw)
        ).fetchall()
        return rows

    def get_by_id(self, auction_id):
        db = get_db()
        row = db.execute(
            """
            SELECT id, title, category, description, starting_bid, end_datetime
            FROM auctions
            WHERE id = ?
            """,
            (auction_id,)
        ).fetchone()
        return row

    def create_auction(self, title, category, description, starting_bid, end_datetime):
        db = get_db()
        db.execute(
            """
            INSERT INTO auctions (title, category, description, starting_bid, end_datetime)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, category, description, starting_bid, end_datetime)
        )
        db.commit()

    def update_auction(self, auction_id, title, category, description, starting_bid, end_datetime):
        db = get_db()
        db.execute(
            """
            UPDATE auctions
            SET title = ?, category = ?, description = ?, starting_bid = ?, end_datetime = ?
            WHERE id = ?
            """,
            (title, category, description, starting_bid, end_datetime, auction_id)
        )
        db.commit()

    def delete_auction(self, auction_id):
        db = get_db()
        # remove related data first
        db.execute("DELETE FROM bids WHERE auction_id = ?", (auction_id,))
        db.execute("DELETE FROM reactions WHERE auction_id = ?", (auction_id,))
        db.execute("DELETE FROM auctions WHERE id = ?", (auction_id,))
        db.commit()

    # -------- Bids --------

    def get_top_bids(self, auction_id, limit=2):
        db = get_db()
        rows = db.execute(
            """
            SELECT bidder_email, bid_amount, bid_datetime
            FROM bids
            WHERE auction_id = ?
            ORDER BY bid_amount DESC, bid_datetime DESC
            LIMIT ?
            """,
            (auction_id, limit)
        ).fetchall()
        return rows

    def add_bid(self, auction_id, bidder_email, bid_amount):
        db = get_db()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        db.execute(
            """
            INSERT INTO bids (auction_id, bidder_email, bid_amount, bid_datetime)
            VALUES (?, ?, ?, ?)
            """,
            (auction_id, bidder_email, bid_amount, now_str)
        )
        db.commit()

    def delete_bids_for_auction(self, auction_id):
        db = get_db()
        db.execute(
            "DELETE FROM bids WHERE auction_id = ?",
            (auction_id,)
        )
        db.commit()
