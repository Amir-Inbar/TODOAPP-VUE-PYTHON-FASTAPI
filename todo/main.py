from fastapi import FastAPI, Request
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .routes import todo, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# app.include_router(authentication.router)
app.include_router(todo.router)
app.include_router(user.router)
