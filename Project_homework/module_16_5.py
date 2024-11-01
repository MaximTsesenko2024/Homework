from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel

api = FastAPI()

templates = Jinja2Templates(directory='templates')


users = []


class User(BaseModel):
    id: int = None  # номер пользователя
    username: str = ''  # - имя пользователя
    age: int = 0  # возраст пользователя

@api.get('/')
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@api.get(path='/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    index = None
    for i in range(len(users)):
        if users[i].id == user_id:
            index = i
            break
    if index is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": users[index]})


@api.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=45)]) -> User:
    user_id = users[-1].id + 1 if len(users) > 0 else 1
    new_user = User()
    new_user.id = user_id
    new_user.username = username
    new_user.age = age
    users.append(new_user)
    return new_user


@api.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(gt=0, le=120, description='Enter User ID', example=30)],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=45)]) -> User:
    index = None
    for i in range(len(users)):
        if users[i].id == user_id:
            index = i
            break
    if index is None:
        raise HTTPException(status_code=404, detail="User not found")
    users[index].username = username
    users[index].age = age
    return users[index]


@api.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(gt=0, le=120, description='Enter User ID', example=30)]) -> User:
    index = None
    for i in range(len(users)):
        if users[i].id == user_id:
            index = i
            break
    if index is None:
        raise HTTPException(status_code=404, detail="User was not found")
    user = users.pop(index)
    return user
