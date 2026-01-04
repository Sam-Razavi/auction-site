from flask import render_template
from app.auctions import auctions_bp

@auctions_bp.route("/")
def auction_list():
    auctions = [
        {
            "id": 1,
            "title": "Vintage Camera",
            "category": "Electronics",
            "starting_bid": 100,
            "end_datetime": "2026-01-10 18:00",
        },
        {
            "id": 2,
            "title": "Coffee Table",
            "category": "Home",
            "starting_bid": 200,
            "end_datetime": "2026-01-08 12:00",
        },
    ]

    return render_template("auctions/list.html", auctions=auctions)
