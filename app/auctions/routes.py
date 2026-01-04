from flask import render_template, abort
from app.auctions import auctions_bp
from app.repositories.auction_repository import AuctionRepository
from flask import render_template, abort, request, redirect, url_for, flash


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

    top_bids = repo.get_top_bids(auction_id)

    return render_template("auctions/detail.html", auction=auction, top_bids=top_bids)

@auctions_bp.route("/auctions/<int:auction_id>/bid", methods=["POST"])
def place_bid(auction_id):
    auction = repo.get_by_id(auction_id)
    if auction is None:
        abort(404)

    bidder_email = request.form.get("bidder_email", "").strip()
    bid_amount_str = request.form.get("bid_amount", "").strip()

    # very simple validation (student level)
    if bidder_email == "" or bid_amount_str == "":
        flash("Please enter email and bid amount.")
        return redirect(url_for("auctions.auction_detail", auction_id=auction_id))

    try:
        bid_amount = int(bid_amount_str)
    except ValueError:
        flash("Bid amount must be a number.")
        return redirect(url_for("auctions.auction_detail", auction_id=auction_id))

    repo.add_bid(auction_id, bidder_email, bid_amount)
    flash("Your bid was placed!")
    return redirect(url_for("auctions.auction_detail", auction_id=auction_id))


