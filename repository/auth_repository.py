from models.user import User, AuthUser, UserDB
from exceptions.bad_400 import http_400_with_header, http_400_bad_request
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
# this code generate more security

oauth2 = OAuth2PasswordBearer(tokenUrl="auth")

users_list = {
  "Devin":{
    "username": "DevCoro",
    "name": "Devian Coro",
    "last_name": "Cerez",
    "age": 32,
    "email": "dev@email.com",
    "disable": True,
    "password": "root"
  },
  "liv":{
    "username": "DevRerea",
    "name": "Liv Rerez",
    "last_name": "Curtos",
    "age": 23,
    "email": "DevRC@email.com",
    "disable": False,
    "password": "root2"
  },
}


def search_data(username: str):
    if username in users_list:
        user_data = users_list[username]
        return AuthUser(username=str(user_data["username"]), password=str(user_data["password"]))

def search_user(username:str):
    if username in users_list:
        user_data = users_list[username]
        return User(
            username=str(user_data["username"]),
            name=str(user_data["name"]),
            last_name=str(user_data["last_name"]),
            age = int(str(user_data["age"])),
            email=str(user_data["email"]),
            disable=bool(user_data["disable"])
        )

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        http_400_with_header("User not Authorized")
    if user.disable:
       http_400_bad_request("El usuario no esta activo")
    return user

