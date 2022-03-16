from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from . import models
from .database import engine
from .routers import task, user, auth


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.router)


@app.get('/')
def index():
    return {"data": [{"do it": "Praise the Lord! Bless the Lord! Bless His Holy Name! Forever! \
Forever and Ever! Amen!"}, {"John 16,33": "I have told you these things, so that in Me you may have [perfect] peace. In the world (in this world) you (will) have (trouble) tribulation and distress and suffering, but be courageous [be confident, be undaunted, be filled with joy]; [but take heart!] I have overcome the world! [My conquest is accomplished, My victory abiding.]"}]}


app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/user/dabzse', response_class=HTMLResponse, tags=['Admin'])
def get_super(request: Request):
    return templates.TemplateResponse("dabzse.html", {"request": request})


app.include_router(task.router)
app.include_router(user.router)
