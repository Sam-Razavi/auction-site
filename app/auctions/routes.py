from flask import render_template, abort
from app.auctions import auctions_bp
from app.repositories.auction_repository import AuctionRepository

repo = AuctionRepository()

@auctions_bp.route("/")
def auction_list():
    auctions = repo.get_all()
    return render_template("auctions/list.html", auctions=auctions)

@auctions_bp.route("/auctions/<int:auction_id>")
def auction_detail(auction_id):
    auction = repo.get_by_id(auction_id)

    if auction is None:
        abort(404)

    return render_template("auctions/detail.html", auction=auction)
