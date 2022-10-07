from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class TodoBase(BaseModel):
    title: str
    description: str
    createdAt: datetime
    doneAt: Optional[datetime] or None
    status: str


class Todo(TodoBase):
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    todos: List[Todo] = []

    class Config:
        orm_mode = True


class ShowTodo(BaseModel):
    title: str
    description: str
    createdAt: datetime
    doneAt:Optional[datetime]
    status: str
    creator: ShowUser
    id: int

    class Config:
        orm_mode = True


class login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
