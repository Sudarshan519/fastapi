from fastapi import APIRouter, Depends,status,HTTPException,Response
import schemas,database,models
from typing import List
from sqlalchemy.orm import Session
get_db=database.get_db
from hashing import Hash
router=APIRouter(tags=['users'])
@router.post('/user',response_model=schemas.ShowUser,tags=['User'])
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    new_user=models.User(username=request.username,email=request.email,password=Hash.hashed_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}',response_model=schemas.ShowUser,tags=['User'])
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id {id} not found')
    return user