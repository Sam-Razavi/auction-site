from datetime import datetime
from app.db import get_db


class AuctionRepository:
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
