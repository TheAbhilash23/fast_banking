import sys

from databases import Database
from rich.ansi import stdout
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# PostgreSQL database URL
DATABASE_URL = "postgresql+asyncpg://admin:root@fast_banking_db/fast_banking"

# SQLAlchemy Base for ORM models
Base = declarative_base()

# Create a Database instance (used with async)
database = Database(DATABASE_URL)

# Create engine and session for migrations or sync operations
engine = create_engine(DATABASE_URL.replace("+asyncpg", ""))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
