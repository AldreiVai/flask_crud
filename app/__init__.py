from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate
from .models.notes_model import Notes
from .routes.notes_routes import notes_bp
from .api.notes_api import notes_api_bp
import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    load_dotenv()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(notes_bp)
    app.register_blueprint(notes_api_bp)

    with app.app_context():
        db.create_all()

    return app