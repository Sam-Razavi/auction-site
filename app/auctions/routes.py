from flask import render_template, abort
from app.auctions import auctions_bp
from app.repositories.auction_repository import AuctionRepository
from flask import render_template, abort, request, redirect, url_for, flash


repo = AuctionRepository()

@auctions_bp.route("/")
def auction_list():
    q = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()
    min_price_str = request.args.get("min_price", "").strip()
    max_price_str = request.args.get("max_price", "").strip()
    end_before = request.args.get("end_before", "").strip()

    # convert price inputs (student simple)
    min_price = None
    max_price = None

    if min_price_str != "":
        try:
            min_price = int(min_price_str)
        except ValueError:
            min_price = None

    if max_price_str != "":
        try:
            max_price = int(max_price_str)
        except ValueError:
            max_price = None

    categories = repo.get_categories()

    # if any filter is used -> filter first
    if category or min_price is not None or max_price is not None or end_before:
        auctions = repo.filter_auctions(
            category=category if category else None,
            min_price=min_price,
            max_price=max_price,
            end_before=end_before if end_before else None
        )

        # if q is also used, do a simple in-python filter (easy student solution)
        if q:
            q_lower = q.lower()
            auctions = [a for a in auctions if q_lower in a["title"].lower() or q_lower in a["description"].lower()]

    else:
        # no filters -> normal search or all
        if q:
            auctions = repo.search(q)
        else:
            auctions = repo.get_all()

    return render_template(
        "auctions/list.html",
        auctions=auctions,
        q=q,
        categories=categories,
        category=category,
        min_price=min_price_str,
        max_price=max_price_str,
        end_before=end_before
    )


@auctions_bp.route("/auctions/<int:auction_id>")
def auction_detail(auction_id):
    auction = repo.get_by_id(auction_id)
    if auction is None:
        abort(404)

    top_bids = repo.get_top_bids(auction_id)
    likes, dislikes = repo.get_reaction_counts(auction_id)

    return render_template(
        "auctions/detail.html",
        auction=auction,
        top_bids=top_bids,
        likes=likes,
        dislikes=dislikes
    )

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

@auctions_bp.route("/auctions/<int:auction_id>/react", methods=["POST"])
def react(auction_id):
    auction = repo.get_by_id(auction_id)
    if auction is None:
        abort(404)

    reaction_type = request.form.get("reaction_type", "")
    if reaction_type not in ["like", "dislike"]:
        flash("Invalid reaction.")
        return redirect(url_for("auctions.auction_detail", auction_id=auction_id))

    repo.add_reaction(auction_id, reaction_type)
    flash("Thanks for your feedback!")
    return redirect(url_for("auctions.auction_detail", auction_id=auction_id))



