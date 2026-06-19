
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace with your PostgreSQL username, password, and database name
DATABASE_URL = "postgresql://postgres:1423@localhost/library_db"

# Create database engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
Base = declarative_base()

# Dependency for database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
