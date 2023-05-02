from fastapi import APIRouter, Depends,status,HTTPException,Response
import schemas,database,models,oauth2
# from database import get_db
from typing import List
from sqlalchemy.orm import Session
from repository import blog

router=APIRouter(prefix='/blog',tags=['blogs'])
get_db=database.get_db
@router.get('/',response_model=List[schemas.ShowBlog],tags=['blogs'])
def all(db:Session=Depends(database.get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
    # blogs=db.query(models.Blog).all()
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED,tags=['blogs'])
def create(request:schemas.Blog,db:Session=Depends(get_db)):
    return blog.create(request,db)
    # new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    # return request
    # return "creating"

@router.get('/{id}',response_model=schemas.ShowBlog)
def show(id:int,response:Response,db:Session=Depends(get_db)):
    return blog.get(id,db)
    # blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not available")
    #     response.status_code=status.HTTP_404_NOT_FOUND
    #     return {'detail':f"Blog with id {id} is not available"}
    # return blog

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
    return blog.destroy(id,db)
    # blog=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    # db.commit()
    # return 'done'


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
    return blog.update(id,request,db)
    # blog=db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
    # blog.update(request.dict())
    
    # db.commit()
    # return 'updated'