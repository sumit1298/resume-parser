import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool


DATABASE_URL = (
    "postgresql+psycopg2://"
    "postgres.roqiyrlmjpgjuxadwwlj:Vsn1vsm%408979"
    "@aws-1-ap-south-1.pooler.supabase.com:6543/postgres"
    "?sslmode=require"
)

engine = create_engine(
    DATABASE_URL,
    poolclass=NullPool,   # REQUIRED for Supabase pooler
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
