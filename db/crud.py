from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException, File
import os

def get_user_id(db: Session, user_id: int):
    return db.query(models.DBUser).filter(models.DBUser.id == user_id).first()

def get_user(db: Session, skip: int = 0, limit = 100):
    return db.query(models.DBUser).offset(skip).limit(limit).all

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.DBUser(username = user.username, email = user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user