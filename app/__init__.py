from flask import Flask
from app.db import close_db


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["SECRET_KEY"] = "dev"
    app.config["ADMIN_PASSWORD"] = "admin123"

    try:
        import os
        os.makedirs(app.instance_path, exist_ok=True)
    except Exception:
        pass

    app.teardown_appcontext(close_db)

    from app.auctions import auctions_bp
    app.register_blueprint(auctions_bp)

    from app.admin import admin_bp
    app.register_blueprint(admin_bp)

    return app
