
import models,schemas 
from fastapi import Depends, FastAPI
from pydantic import BaseModel


from database import SessionLocal,engine
from sqlalchemy.orm import Session
models.Base.metadata.create_all(engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

app=FastAPI()


@app.get('/blog')
def all(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.post('/blog')
def create(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    return request
    return "creating"

@app.get('/blog/{id}')
def show(id:int,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    return blog