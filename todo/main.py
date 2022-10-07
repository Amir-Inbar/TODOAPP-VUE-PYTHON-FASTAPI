from fastapi import FastAPI, Request
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .routes import todo, user, authentication
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

models.Base.metadata.create_all(engine)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

templates = Jinja2Templates(directory="public")
app.mount("./public", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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
