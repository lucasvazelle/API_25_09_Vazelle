from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class User(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None


# Simuler une base de données en mémoire
fake_db_items = {}
fake_db_users = {}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = fake_db_items.get(item_id)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items/")
def create_item(item: Item):
    item_id = len(fake_db_items) + 1
    fake_db_items[item_id] = item
    return {"item_id": item_id, **item.dict()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in fake_db_items:
        fake_db_items[item_id] = item
        return {"item_id": item_id, **item.dict()}
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in fake_db_items:
        del fake_db_items[item_id]
        return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/users/{username}")
def read_user(username: str):
    user = fake_db_users.get(username)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users/")
def create_user(user: User):
    if user.username in fake_db_users:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_db_users[user.username] = user
    return {"username": user.username, **user.dict()}


@app.delete("/users/{username}")
def delete_user(username: str):
    if username in fake_db_users:
        del fake_db_users[username]
        return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
