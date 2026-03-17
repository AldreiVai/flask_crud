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
```

## .env
```
DATABASE_URL=postgresql://postgres:password@localhost:5432/flask_crud
DOCKER_DB_CONNECTION=postgresql://postgres:password@db:5432/flask_crud
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=flask_crud

```
## Then run:
```
flask db upgrade
flask run
```

For running in Docker:
docker compose up --build
