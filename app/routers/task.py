from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models, oauth2


use_db = database.use_db

router = APIRouter(
    prefix='/task',
    tags=['Tasks']
)



@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowTask])
def browse(db: Session = Depends(use_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return db.query(models.Task).all()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(task: schemas.Task, db: Session = Depends(use_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_task = models.Task(title=task.title, body=task.body, user_id=1)
    # ! user_id is now hard-coded for test only
    ## should be the logged in user_id
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowTask)
def show(id: int, db: Session = Depends(use_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if not task:
#        response.status_code = status.HTTP_404_NOT_FOUND
#        return {'detail': f'The task with the id ({id}) was not found'}
## or use the line above instead
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The task with the id ({id}) was not found')
    return task
## ! unfortunately returns all the jobs ! have to fix....


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(use_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    task = db.query(models.Task).filter(models.Task.id == id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Task with id ({id}) not found')
    task.delete(synchronize_session=False)
    db.commit()
    return 'The task has been deleted successfully'


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Task, db: Session = Depends(use_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    ## ! find the bug
    task = db.query(models.Task).filter(models.Task.id == id)
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Task with id ({id}) not found')
    task.update(request.dict())
    db.commit()
    return 'The task has been updated successfully'

