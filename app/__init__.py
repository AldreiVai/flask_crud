from flask import Flask
from .extensions import db, migrate
from .models.notes_model import Notes
from .routes.notes_routes import notes_bp
import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    load_dotenv()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(notes_bp)

    with app.app_context():
        db.create_all()

    return app