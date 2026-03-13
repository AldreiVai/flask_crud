from flask import Flask
from .extensions import db, migrate
from .models.notes_model import Notes
from .routes.notes_routes import notes_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:password@localhost:5432/flask_crud"

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(notes_bp)

    return app