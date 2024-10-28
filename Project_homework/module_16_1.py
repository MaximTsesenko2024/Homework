from fastapi import FastAPI


api = FastAPI()


@api.get('/')
async def welcome() -> str:
    return "Главная страница"


@api.get('/user/admin')
async def admin() -> str:
    return "Вы вошли как администратор"


@api.get('/user/{user_id}')
async def users(user_id: str) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@api.get('/user/')
async def info(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
