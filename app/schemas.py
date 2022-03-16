from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    body: str


class Task(TaskBase):
    class Config():
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    jobs: list[Task] = []
    class Config():
        orm_mode = True


class ShowTask(BaseModel):
    title: str
    body: str
    owner: UserBase
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
