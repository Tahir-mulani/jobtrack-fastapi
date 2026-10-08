# JobTrack

Production-style Job Application Tracker built with FastAPI, SQLAlchemy, PostgreSQL, JWT authentication, and a responsive HTML/CSS/JavaScript frontend.

## Features

- JWT authentication
- Argon2 password hashing
- User registration/login/profile
- Role-based users/admin
- Companies CRUD
- Jobs CRUD
- Job application tracking
- Interview tracking
- Dashboard statistics
- Search/filter applications
- Pydantic validation
- SQLAlchemy ORM
- Alembic migrations
- Centralized exception handling
- Logging
- CORS configuration
- Pytest API tests
- Vercel deployment configuration
- PostgreSQL-ready production configuration

## Local setup

1. Create a PostgreSQL database, for example `jobtrack`.
2. Copy `.env.example` to `.env`.
3. Set `DATABASE_URL` and `SECRET_KEY`.
4. Create a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

5. Install:

```bash
pip install -r requirements.txt
```

6. Run migrations:

```bash
alembic upgrade head
```

7. Start:

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

Swagger: `http://127.0.0.1:8000/docs`

## Vercel

The API entry point is `api/index.py`. Set the same environment variables in Vercel.

Use an external managed PostgreSQL provider such as Neon or Supabase. Do not rely on the Vercel filesystem for persistent data.

## Important

This repository is designed as a portfolio/production-style project. Before commercial production, add HTTPS/domain configuration, stronger operational monitoring, secret rotation, database backups, rate limiting/WAF, email verification/password reset, and CI/CD security scanning.
