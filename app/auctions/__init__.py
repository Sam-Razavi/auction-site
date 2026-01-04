from flask import Blueprint

auctions_bp = Blueprint(
    "auctions",
    __name__,
    template_folder="templates"
)

from app.auctions import routes
