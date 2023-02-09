from fastapi import Request, Depends
from sqlalchemy.orm import Session
from todo.main import app, templates
from database.base import get_db
from models import ToDo
from todo.config import Settings

from starlette.status import HTTP_303_SEE_OTHER
from starlette.responses import RedirectResponse


@app.get('/')
def home(request: Request, db_session: Session = Depends(get_db)):
    todos = db_session.query(ToDo).all()
    return templates.TemplateResponse('todo/index.html',
                                      {'request': request,
                                       'app_name': Settings.app_name,
                                       'todo_list': todos})


