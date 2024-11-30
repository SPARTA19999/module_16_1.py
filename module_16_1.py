from fastapi import FastAPI
from typing import Optional

# Создаем приложение
app = FastAPI()

# Маршрут для главной страницы
@app.get("/")
def read_main():
    return {"message": "Главная страница"}

# Маршрут для страницы администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

# Маршрут для страниц пользователей с параметром user_id
@app.get("/user/{user_id}")
def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут для страниц пользователей с передачей данных через адресную строку
@app.get("/user")
def user_info(username: Optional[str] = None, age: Optional[int] = None):
    if username and age:
        return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
    return {"message": "Пожалуйста, укажите имя и возраст пользователя."}
