from fastapi import FastAPI
from login import login_simple

auth = FastAPI()

auth.include_router(login_simple.login_simple)
#@auth.get("/") #Ruta raiz debe de ir aqui
#async def hello_proof():
#    return "hello"


