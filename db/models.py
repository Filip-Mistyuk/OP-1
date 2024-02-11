from sqlalchemy import Column, Integer, String
from .engine import Base

class DBUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, unique=False, nullable=False)
    email = Column(String, unique=True, nullable=False)
