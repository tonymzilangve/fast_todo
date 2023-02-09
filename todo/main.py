from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from .routes import home

app = FastAPI()
app.mount('/static', StaticFiles(directory='todo/static'), name='static')
templates = Jinja2Templates(directory='todo/templates')

