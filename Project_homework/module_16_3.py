from fastapi import FastAPI, Path
from typing import Annotated

api = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@api.get('/')
async def get_main_page() -> str:
    return "Главная страница"


@api.get('/users')
async def get_all_users() -> dict:
    return users


@api.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=45)]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f"User {user_id} is registered"


@api.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[str, Path(min_length=1, max_length=20, description='Enter User ID', example='30')],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=45)]) -> str:
    if user_id in users.keys():
        users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f"The user {user_id} is registered"


@api.delete('/user/{user_id}')
async def delete_user(
        user_id: str = Path(min_length=1, max_length=20, description='Enter User ID', example='30')) -> str:
    users.pop(user_id)
    return f"The user {user_id} was deleted"
