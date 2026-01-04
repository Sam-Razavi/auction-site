from flask import render_template, request, redirect, url_for, flash, session
from app.admin import admin_bp
from app.repositories.auction_repository import AuctionRepository

repo = AuctionRepository()

def require_admin():
    if not session.get("is_admin"):
        flash("You need to login as admin.")
        return False
    return True

@admin_bp.route("/admin/auctions")
def admin_auctions():
    if not require_admin():
        return redirect(url_for("admin.login"))

    auctions = repo.get_all()
    return render_template("admin/auctions.html", auctions=auctions)

@admin_bp.route("/admin/auctions/create", methods=["GET", "POST"])
def admin_create_auction():
    if not require_admin():
        return redirect(url_for("admin.login"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        category = request.form.get("category", "").strip()
        description = request.form.get("description", "").strip()
        starting_bid = request.form.get("starting_bid", "").strip()
        end_datetime = request.form.get("end_datetime", "").strip()

        if title == "" or category == "" or description == "" or starting_bid == "" or end_datetime == "":
            flash("Please fill in all fields.")
            return render_template("admin/auction_form.html", auction=None)

        try:
            starting_bid_int = int(starting_bid)
        except ValueError:
            flash("Starting bid must be a number.")
            return render_template("admin/auction_form.html", auction=None)

        repo.create_auction(title, category, description, starting_bid_int, end_datetime)
        flash("Auction created.")
        return redirect(url_for("admin.admin_auctions"))

    return render_template("admin/auction_form.html", auction=None)

@admin_bp.route("/admin/auctions/<int:auction_id>/edit", methods=["GET", "POST"])
def admin_edit_auction(auction_id):
    if not require_admin():
        return redirect(url_for("admin.login"))

    auction = repo.get_by_id(auction_id)
    if auction is None:
        flash("Auction not found.")
        return redirect(url_for("admin.admin_auctions"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        category = request.form.get("category", "").strip()
        description = request.form.get("description", "").strip()
        starting_bid = request.form.get("starting_bid", "").strip()
        end_datetime = request.form.get("end_datetime", "").strip()

        if title == "" or category == "" or description == "" or starting_bid == "" or end_datetime == "":
            flash("Please fill in all fields.")
            return render_template("admin/auction_form.html", auction=auction)

        try:
            starting_bid_int = int(starting_bid)
        except ValueError:
            flash("Starting bid must be a number.")
            return render_template("admin/auction_form.html", auction=auction)

        repo.update_auction(auction_id, title, category, description, starting_bid_int, end_datetime)
        flash("Auction updated.")
        return redirect(url_for("admin.admin_auctions"))

    return render_template("admin/auction_form.html", auction=auction)

@admin_bp.route("/admin/auctions/<int:auction_id>/delete", methods=["POST"])
def admin_delete_auction(auction_id):
    if not require_admin():
        return redirect(url_for("admin.login"))

    repo.delete_auction(auction_id)
    flash("Auction deleted.")
    return redirect(url_for("admin.admin_auctions"))
