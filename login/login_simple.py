from fastapi import APIRouter, Depends
# ?: why? this library:
from fastapi.security import  OAuth2PasswordRequestForm
from exceptions.bad_400 import http_400_bad_request
from repository.auth_repository import users_list, search_data, search_user, current_user
from models.user import User


# if pinned the prefix
login_simple = APIRouter(prefix="/login_simple", tags=["login simple"])

@login_simple.post("/auth")
async def authentication(form: OAuth2PasswordRequestForm = Depends()):
    user_db=users_list.get(form.username)

    if not user_db:
        http_400_bad_request("user not found")
    user = search_data(form.username)

    if not form.password == user.password:
        http_400_bad_request("password is incorrect")

    return {"access_token": user.username, "token_type":"bearer"}


@login_simple.get("/users/me")
async def me(user: User = Depends(current_user)):
  #retorn user 
  return user



