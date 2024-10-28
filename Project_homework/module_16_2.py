from fastapi import FastAPI, Path
from typing import Annotated

api = FastAPI()


@api.get('/')
async def welcome() -> str:
    return "Главная страница"


@api.get('/user/admin')
async def admin() -> str:
    return "Вы вошли как администратор"


@api.get('/user/{user_id}')
async def users(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=30)) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@api.get('/user/{username}/{age}')
async def info(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=45)]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


"""
username - строка, age - целое число.
username ограничение по длине: больше или равно 5 и меньше либо равно 20.
age ограничение по значению: больше или равно 18 и меньше либо равно 120.
Описания для username и age - 'Enter username' и 'Enter age' соответственно.
Примеры для username и age - 'UrbanUser' и '24' соответственно. (можете подставить свои примеры не противоречащие валидации).
"""
