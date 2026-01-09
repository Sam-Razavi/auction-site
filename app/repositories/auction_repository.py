from datetime import datetime
from app.db import get_db


class AuctionRepository:
    # -------- Auctions --------

    def get_all(self, sort="soon"):
        db = get_db()
        order = "ASC" if sort == "soon" else "DESC"
        rows = db.execute(
            f"""
            SELECT id, title, category, description, starting_bid, end_datetime, image_filename
            FROM auctions
            ORDER BY end_datetime {order}
            """
        ).fetchall()
        return rows

    def get_by_id(self, auction_id):
        db = get_db()
        row = db.execute(
            """
            SELECT id, title, category, description, starting_bid, end_datetime, image_filename
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
        db.execute("DELETE FROM bids WHERE auction_id = ?", (auction_id,))
        db.commit()

    def get_bid_count(self, auction_id):
        db = get_db()
        row = db.execute(
            "SELECT COUNT(*) AS cnt FROM bids WHERE auction_id = ?",
            (auction_id,)
        ).fetchone()
        return row["cnt"] if row else 0

    # -------- Reactions --------

    def get_reaction_counts(self, auction_id):
        db = get_db()
        likes_row = db.execute(
            "SELECT COUNT(*) AS cnt FROM reactions WHERE auction_id = ? AND reaction_type = 'like'",
            (auction_id,)
        ).fetchone()
        dislikes_row = db.execute(
            "SELECT COUNT(*) AS cnt FROM reactions WHERE auction_id = ? AND reaction_type = 'dislike'",
            (auction_id,)
        ).fetchone()

        likes = likes_row["cnt"] if likes_row else 0
        dislikes = dislikes_row["cnt"] if dislikes_row else 0
        return likes, dislikes

    def add_reaction(self, auction_id, reaction_type):
        db = get_db()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        db.execute(
            """
            INSERT INTO reactions (auction_id, reaction_type, created_at)
            VALUES (?, ?, ?)
            """,
            (auction_id, reaction_type, now_str)
        )
        db.commit()

    # -------- Search / Filters --------

    def search(self, keyword, sort="soon"):
        db = get_db()
        order = "ASC" if sort == "soon" else "DESC"
        kw = f"%{keyword}%"
        rows = db.execute(
            f"""
            SELECT id, title, category, description, starting_bid, end_datetime, image_filename
            FROM auctions
            WHERE title LIKE ? OR description LIKE ?
            ORDER BY end_datetime {order}
            """,
            (kw, kw)
        ).fetchall()
        return rows

    def get_categories(self):
        db = get_db()
        rows = db.execute(
            """
            SELECT DISTINCT category
            FROM auctions
            ORDER BY category ASC
            """
        ).fetchall()
        return [r["category"] for r in rows]

    def filter_auctions(self, category=None, min_price=None, max_price=None, end_before=None, sort="soon"):
        db = get_db()
        order = "ASC" if sort == "soon" else "DESC"

        sql = """
            SELECT id, title, category, description, starting_bid, end_datetime, image_filename
            FROM auctions
            WHERE 1=1
        """
        params = []

        if category:
            sql += " AND category = ?"
            params.append(category)

        if min_price is not None:
            sql += " AND starting_bid >= ?"
            params.append(min_price)

        if max_price is not None:
            sql += " AND starting_bid <= ?"
            params.append(max_price)

        if end_before:
            sql += " AND end_datetime <= ?"
            params.append(end_before)

        sql += f" ORDER BY end_datetime {order}"

        rows = db.execute(sql, tuple(params)).fetchall()
        return rows
