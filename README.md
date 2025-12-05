# Tourism API Backend

A FastAPI-based backend for the Tourism application with PostgreSQL database, SQLAlchemy ORM, and Alembic migrations.

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── auth.py           # Authentication endpoints
│   ├── core/
│   │   ├── config.py             # Configuration settings
│   │   └── security.py           # Password hashing & JWT tokens
│   ├── db/
│   │   ├── base.py               # SQLAlchemy Base
│   │   └── session.py            # Database session management
│   ├── models/
│   │   └── user.py               # User model
│   ├── schemas/
│   │   └── user.py               # Pydantic schemas
│   └── crud/
│       └── user.py               # CRUD operations
├── alembic/                       # Database migrations
├── main.py                        # Application entry point
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables
└── .gitignore                     # Git ignore rules
```

## Setup Instructions

### 1. Prerequisites

- Python 3.9+
- PostgreSQL 12+
- pip or conda

### 2. Install Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment

Edit `.env` file with your PostgreSQL credentials:

```env
ENVIRONMENT=development
DEBUG=True
DATABASE_URL=postgresql://username:password@localhost:5432/tourism_db
SECRET_KEY=your-super-secret-key-change-this-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 4. Create Database

Create a PostgreSQL database:

```sql
CREATE DATABASE tourism_db;
```

### 5. Run Migrations

```bash
cd backend
source venv/bin/activate
alembic upgrade head
```

Or create a new migration for the User model:

```bash
alembic revision --autogenerate -m "Add user table"
alembic upgrade head
```

### 6. Run the Server

```bash
source venv/bin/activate
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### 7. API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Authentication

- **POST** `/api/register` - Register a new user
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword"
  }
  ```

- **POST** `/api/login` - Login user
  ```json
  {
    "email": "john@example.com",
    "password": "securepassword"
  }
  ```

- **GET** `/api/health` - Health check

## Database Migrations with Alembic

### Create a new migration

```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations

```bash
alembic upgrade head
```

### Rollback migrations

```bash
alembic downgrade -1
```

### View migration history

```bash
alembic current
alembic history
```

## Features

- ✅ User authentication with JWT tokens
- ✅ Password hashing with bcrypt
- ✅ SQLAlchemy ORM with PostgreSQL
- ✅ Alembic database migrations
- ✅ Environment-based configuration
- ✅ CORS support for frontend integration
- ✅ Pydantic validation schemas
- ✅ Organized folder structure following best practices

## Security Considerations

1. **Secret Key**: Change the `SECRET_KEY` in production
2. **Database**: Use strong PostgreSQL passwords
3. **CORS**: Update `allow_origins` for production domains
4. **Tokens**: Adjust `ACCESS_TOKEN_EXPIRE_MINUTES` as needed
5. **.env**: Never commit `.env` to version control

## Development

To add new endpoints:

1. Create schema in `app/schemas/`
2. Create model in `app/models/`
3. Create CRUD operations in `app/crud/`
4. Create routes in `app/api/routes/`
5. Include the router in `main.py`

## Troubleshooting

### PostgreSQL Connection Error

Ensure PostgreSQL is running and the DATABASE_URL is correct.

### Alembic Issues

Clear `__pycache__` and recreate the migration:

```bash
find . -type d -name __pycache__ -exec rm -r {} +
alembic revision --autogenerate -m "Your message"
```

## License

MIT
