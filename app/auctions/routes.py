from flask import render_template
from app.auctions import auctions_bp

@auctions_bp.route("/")
def auction_list():
    return render_template("auctions/list.html")
