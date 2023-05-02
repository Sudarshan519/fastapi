from datetime import timedelta
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from hashing import Hash
from auth_token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
router=APIRouter(prefix='/auth',tags=['authentication'])

import schemas,database,models
@router.post('/login' )
def login(request:schemas.Login,db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Credentials')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Credentials.')
    # generate a jwt token and return
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
    return user
    return 'login'