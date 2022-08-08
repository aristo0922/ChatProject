from typing import Union
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}

class User(BaseModel):
    id: int
    name: str
    password: str
    desc : Union[str, None] = None

@app.get("/users/{user_id}")
def read_user(user_id: int, q: Union[str, None] = Query(
    default=None, min_length=3, max_length=50, regex="^fixedquery"
)):
    return {"user_id" : user_id, "q":q}

@app.put("/users/{user_id}")
def upgrade_user(user_id:int, user:User):
    return {"user_name": user.name, "user_id": user.id}

@app.post("/create/users")
async def create_user(user:User):
    return user