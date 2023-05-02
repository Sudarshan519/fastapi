
from typing import List
import models,schemas 
from fastapi import Depends, FastAPI,status,Response,HTTPException
from pydantic import BaseModel

from hashing import Hash
from database import SessionLocal,engine,get_db
from sqlalchemy.orm import Session
from routers import blog,user,authentication
models.Base.metadata.create_all(engine)


# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

app=FastAPI()
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
# @app.get('/blog',response_model=List[schemas.ShowBlog])
# def all(db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

# @app.post('/blog',status_code=status.HTTP_201_CREATED)
# def create(request:schemas.Blog,db:Session=Depends(get_db)):
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog
#     return request
#     return "creating"

# @app.get('/blog/{id}',response_model=schemas.ShowBlog)
# def show(id:int,response:Response,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not available")
#         response.status_code=status.HTTP_404_NOT_FOUND
#         return {'detail':f"Blog with id {id} is not available"}
#     return blog

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
#     db.commit()
#     return 'done'
# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
# def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
#     blog.update(request.dict())
    
#     db.commit()
#     return 'updated'

