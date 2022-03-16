from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models, oauth2
from ..do_hash import MakeHash


use_db = database.use_db

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create(user: schemas.User, db: Session = Depends(use_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_user = models.User(name=user.name, email=user.email, password=MakeHash.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def show(id: int, db: Session = Depends(use_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id ({id}) is not available')
    return user
