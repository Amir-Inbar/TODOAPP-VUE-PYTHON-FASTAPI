from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from todo.database import engine
from todo import models

models.Base.metadata.create_all(engine)

app = FastAPI()

app.mount("./public", StaticFiles(directory="public"), name="public")


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
