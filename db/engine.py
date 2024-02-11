from sqlalchemy import Column, Integer, String
from .engine import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./library.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

sesion_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()