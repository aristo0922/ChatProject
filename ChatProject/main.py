from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}

class User(BaseModel):
    id: int
    name: str
    password: str
    desc : str

@app.get("/users/{user_id}")
def read_user(user_id: int, q: Union[str, None]=None):
    return {"user_id" : user_id
            , "q":q}

@app.put("/users/{user_id}")
def upgrade_user(user_id:int, user:User):
    return {"user_name": user.name, "user_id": user.id}