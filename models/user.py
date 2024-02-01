from pydantic import BaseModel

class User(BaseModel):
    username: str
    name : str
    last_name: str
    age: int
    email: str
    disable: bool

# ?: why?
class UserDB(User):
    password: str

class AuthUser(BaseModel):
    username: str
    password: str

