from fastapi import FastAPI, Path
from typing import Annotated

api = FastAPI()


@api.get('/')
async def get_main_page() -> str:
    return "Главная страница"


@api.get('/user/admin')
async def get_admin_page() -> str:
    return "Вы вошли как администратор"


@api.get('/user/{user_id}')
async def get_users_number(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=30)) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@api.get('/user/{username}/{age}')
async def get_user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=45)]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
