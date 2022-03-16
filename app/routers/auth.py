from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from ..do_hash import MakeHash


router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.use_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Something went wrong!'
        )

    if not MakeHash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid login request!'
        ## ! because we don't want to return the exact problem: incorrect password
        )

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
