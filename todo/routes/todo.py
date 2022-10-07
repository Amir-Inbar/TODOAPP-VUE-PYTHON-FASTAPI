from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import todo

router = APIRouter(
    prefix="/todo",
    tags=['todos']
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowTodo])
# def get_todos(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
def get_todos(db: Session = Depends(get_db)):
    return todo.get_todos(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Todo, db: Session = Depends(get_db)):
    print(request)
           # current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.create(db, request)


@router.get("/{todo_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowTodo)
def get_todo_by_id(todo_id, db: Session = Depends(get_db)):
                   # current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.get_by_id(db, todo_id)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_todo_by_id(todo_id, db: Session = Depends(get_db)):
                      # current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.remove(db, todo_id)


@router.put("/{todo_id}", status_code=status.HTTP_202_ACCEPTED)
def update_todo(todo_id, request: schemas.Todo, db: Session = Depends(get_db)):
                # current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.update(db, todo_id, request)
