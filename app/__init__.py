from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev"

    from app.auctions import auctions_bp
    app.register_blueprint(auctions_bp)

    return app
