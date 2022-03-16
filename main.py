from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
# from typing import Optional
## ! since python3.10 you don't have to import the line above
# import uvicorn
## ! see comment on the bottom of this file


app = FastAPI()

class Task(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str
    active: bool


@app.get('/')
def index():
    return {"data": {"do it": "Praise the Lord! Bless the Lord! Bless His Holy Name! Forever! \
Forever and Ever! Amen!"}}


@app.get('/user')
def get_users(limit=10, active: bool = True, order_by = None):
## ! if you need Optional, so you have python3.6 >= && < python3.10
## use the following function
# def get_users(limit=10, active: bool = True, order_by: Optional[str] = None):
    if active:
        return {"data": f'currently you see only {limit} active users'}
    else:
        return {"data": f'currently you see only {limit} of our all users'}


@app.get('/user/dabzse')
def get_super():
    return {"something about me": [{"personal home page": "http://dabzse.net"}, {"written in/with": "html5/css3/php/mysql"}, {"other page": "https://dabzse-cv.herokuapp.com"}, {"CV extension": "written in/with: python/django"}, {"LinkedIn": "https://linkedin.com/in/dabzse"}, {"anything else?": "married, father, and on the initial release date just turning 40"}]}


@app.get('/user/{id}')
def get_user(id: int):
    return {"data": {"the user's ID is: ": id}}


@app.post('/user')
def create_user(user: User):
    return {"data": f"user is now created with ({user.name}) and ({user.email})"}


@app.post('/task')
def create_task(task: Task):
    return {"data": f"task is created with the following fields: ({task.title}) and ({task.body})"}


@app.get('/task/{id}')
def get_task(id: int):
    return {"data": id}


@app.get('/task/{id}/comments')
def get_task_comments():
    return {"data": {"this is the 1st comment", "this is the 2nd comment", "this is the 3rd comment"}}


@app.get('/about')
def about():
    return {"data": {"this is the about page", "you can find here our team", "also find the contact details on the bottom of the page", "rigth before the footer", "this is the last line"}}


## you can also use the command below to run a server
## instead of :: uvicorn main:app --reload
## recommended for debugging

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
