# Flask + PostgreSQL 

## Libraries Used

### Flask
### Jinja
### Flask-SQLAlchemy
### Flask-Migrate
### psycopg2-binary
### python-dotenv

## Installation
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Add a .env and add DATABASE_URL=postgresql://postgres:password@localhost:5432/db_name
flask db upgrade
flask run
