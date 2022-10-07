from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    createdAt = Column(TIMESTAMP, default=TIMESTAMP)
    doneAt = Column(TIMESTAMP, default=None)
    status = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates="todos")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    todos = relationship('Todo', back_populates="creator")
