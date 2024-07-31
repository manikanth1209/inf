from http.client import HTTPException #exception used to return http error responses,such as 404 0r 500
from typing import Optional  # It is used to indicate that a parameter or return type can be of a specific type or None.
from fastapi import Depends
from models import Base, User #SQLAlchemy models.
from pydantic import BaseModel
from schema import UserSchema
from database import engine,Sessionlocal #engine is the SQLAlchemy engine instance for connecting to the database, and SessionLocal is the session factory for creating database sessions.
from sqlalchemy.orm import Session # Session class, used to manage database transactions and queries.
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)
#The metadata attribute of the Base class holds all the schema definitions (tables, columns, relationships) that have been mapped.
#Purpose:  create_all This method generates the SQL statements needed to create all tables defined in the models.
def get_db():
    try:
        db = Sessionlocal()#creates a new database session.
        yield db # makes the session available to the endpoint function.
    finally:
        db.close()#The finally block ensures db.close() is called to close the session, even if an exception occurs.


app=FastAPI()
@app.post("/adduser")
def add_user(request:UserSchema, db: Session = Depends(get_db)):
    user = User(name=request.name, email=request.email,nickname=request.nickname)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/user/{user_id}")
def get_user(user_id:int,db: Session = Depends(get_db)):
    users = db.query(User).filter(User.id == user_id).first()
    return users

@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        return "User Not Found"
    db.delete(user)
    db.commit()
    return {"detail": "User deleted"}

@app.put("/Users/Update/{id}")
def update_user(user_id: int, user:UserSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db_user.nickname=user.nickname
        db.commit()
        db.refresh(db_user)
        return db_user
    return f"userid:{user_id} not found"