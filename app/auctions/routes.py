from flask import render_template, abort
from app.auctions import auctions_bp

# Dummy data for now (later: SQLite)
AUCTIONS = [
    {
        "id": 1,
        "title": "Vintage Camera",
        "category": "Electronics",
        "description": "Old camera in good condition.",
        "starting_bid": 100,
        "end_datetime": "2026-01-10 18:00",
    },
    {
        "id": 2,
        "title": "Coffee Table",
        "category": "Home",
        "description": "Wooden coffee table. Some small scratches.",
        "starting_bid": 200,
        "end_datetime": "2026-01-08 12:00",
    },
]

@auctions_bp.route("/")
def auction_list():
    return render_template("auctions/list.html", auctions=AUCTIONS)

@auctions_bp.route("/auctions/<int:auction_id>")
def auction_detail(auction_id):
    auction = None
    for a in AUCTIONS:
        if a["id"] == auction_id:
            auction = a
            break

    if auction is None:
        abort(404)

    return render_template("auctions/detail.html", auction=auction)
