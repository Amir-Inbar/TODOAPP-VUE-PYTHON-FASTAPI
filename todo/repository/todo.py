from sqlalchemy.orm import Session
from .. import models
from fastapi import HTTPException, status


def get_todos(db: Session):
    todos = db.query(models.Todo).all()
    return todos


def get_by_id(db: Session, todo_id):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id of {todo_id} is not available")
    return todo


def create(db: Session, request):
    new_todo = models.Todo(title=request.title, createdAt=request.createdAt, status=request.status,
                           doneAt=request.doneAt, description=request.description, user_id=1)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def remove(db: Session, todo_id):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} not found")
    todo.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(db: Session, todo_id: int, request):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} not found")
    todo.update(request.dict())
    db.commit()
    return "updated"
