from fastapi import APIRouter, Depends, status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(db, request)


@router.get('/user_id', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user.get_by_id(db, user_id)
