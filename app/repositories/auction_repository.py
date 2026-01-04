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
