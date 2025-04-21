from typing import Annotated
from faker import Faker
from fastapi import Depends, FastAPI
import uvicorn

from models.user import User
from schemas.user import UserPydantic


faker = Faker()
app = FastAPI()


@app.get("/")
async def home_page():
    return {"message": "hello"}


@app.get("/user/create")
async def create_user():
    user = User.create(
        username=faker.user_name(), password=faker.password(), email=faker.email()
    )
    return user.to_dict()


@app.post("/user/create_concrete")
async def create_user_concrete(user_data: Annotated[UserPydantic ,Depends()]):
    user = User.create(
        **dict(user_data)
    )
    return user.to_dict()


@app.get("/user/{id}")
async def get_user(id: int):
    user: User = User.get(id=id)
    return user.to_dict()


if __name__ == "__main__":
    uvicorn.run("web:app", reload=True)
