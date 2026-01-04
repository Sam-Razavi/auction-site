from flask import Flask
from app.db import close_db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["SECRET_KEY"] = "dev"

    # make sure instance folder exists
    try:
        import os
        os.makedirs(app.instance_path, exist_ok=True)
    except Exception:
        pass

    # close DB when request ends
    app.teardown_appcontext(close_db)

    # register blueprints
    from app.auctions import auctions_bp
    app.register_blueprint(auctions_bp)

    return app
