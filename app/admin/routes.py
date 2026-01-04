from flask import render_template, request, redirect, url_for, flash, session, current_app
from app.admin import admin_bp

@admin_bp.route("/admin/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password", "")

        if password == current_app.config["ADMIN_PASSWORD"]:
            session["is_admin"] = True
            flash("Logged in as admin.")
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Wrong password.")

    return render_template("admin/login.html")

@admin_bp.route("/admin/logout")
def logout():
    session.pop("is_admin", None)
    flash("Logged out.")
    return redirect(url_for("auctions.auction_list"))

@admin_bp.route("/admin")
def dashboard():
    if not session.get("is_admin"):
        flash("You need to login as admin.")
        return redirect(url_for("admin.login"))

    return render_template("admin/dashboard.html")
