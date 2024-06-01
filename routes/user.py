from fastapi.responses import  JSONResponse
from pydantic import BaseModel
from user_jwt import createToken
from fastapi import APIRouter

routeUser = APIRouter()

class User(BaseModel):
    email: str
    password: str


@routeUser.post("/login", tags=["authentication"])
def login(user: User):
    if user.email == "marlon@gmail.com" and user.password == "123":
        token: str = createToken(user.model_dump())
        return token
    return JSONResponse(
        content={
            "message": "Ese usuario no existe",
        }
    )
