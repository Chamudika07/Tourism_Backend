# Backend Setup - Quick Start Guide

## Step-by-Step Setup

### Step 1: Install PostgreSQL

**macOS (using Homebrew):**
```bash
brew install postgresql
brew services start postgresql
```

**Or use Docker:**
```bash
docker run --name postgres-tourism -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:15
```

### Step 2: Create Database

```bash
psql postgres
CREATE DATABASE tourism_db;
\q
```

### Step 3: Activate Virtual Environment

```bash
cd backend
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit `.env` with your PostgreSQL credentials if different.

### Step 6: Initialize Database Schema

```bash
# Create tables from models
python -c "from app.db.session import engine; from app.db.base import Base; Base.metadata.create_all(bind=engine)"
```

Or use Alembic:

```bash
alembic upgrade head
```

### Step 7: Run the Server

```bash
uvicorn main:app --reload
```

Server runs on: **http://localhost:8000**

### Step 8: Test the API

**Register a new user:**
```bash
curl -X POST "http://localhost:8000/api/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

**Login:**
```bash
curl -X POST "http://localhost:8000/api/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

**Health Check:**
```bash
curl http://localhost:8000/api/health
```

## Helpful Links

- API Documentation: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Common Commands

```bash
# Activate virtual environment
source venv/bin/activate

# Deactivate virtual environment
deactivate

# Create new migration
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# View database tables
psql tourism_db -c "\dt"

# Drop database
dropdb tourism_db
```

## Architecture Overview

```
┌─────────────────┐
│  Next.js Client │
│  (Port 3000)    │
└────────┬────────┘
         │ HTTP/REST
         ▼
┌──────────────────────────────┐
│   FastAPI Backend            │
│   (Port 8000)                │
├──────────────────────────────┤
│ app/                         │
│  ├── api/routes/auth.py      │
│  ├── models/user.py          │
│  ├── schemas/                │
│  ├── crud/                   │
│  ├── core/security.py        │
│  └── db/session.py           │
└────────┬────────────────────┘
         │ SQLAlchemy
         ▼
┌──────────────────────────────┐
│   PostgreSQL Database        │
│   (Port 5432)                │
│   tourism_db                 │
└──────────────────────────────┘
```

## What's Included

✅ **User Management**
- Registration with email validation
- Login with JWT tokens
- Password hashing with bcrypt

✅ **Database**
- PostgreSQL with Alembic migrations
- SQLAlchemy ORM
- Automatic table creation

✅ **Security**
- JWT token authentication
- Password hashing
- CORS configuration
- Environment variables

✅ **Folder Structure**
- Clean, scalable architecture
- Separation of concerns
- Easy to extend

## Next Steps

1. Start PostgreSQL
2. Create database `tourism_db`
3. Run `pip install -r requirements.txt`
4. Configure `.env`
5. Run `uvicorn main:app --reload`
6. Visit http://localhost:8000/docs

Happy coding! 🚀
