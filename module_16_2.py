from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()

@app.get("/user/{user_id}")
async def user_id(user_id:Annotated[int, Path(ge=0, le=100, description="Enter User ID", example="25")])-> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def user_info(username:Annotated[str, Path(min_length=5, max_length=20,description="Enter username", example="UrbanUser")]
                    , age:Annotated[int, Path(ge=18,le=120, description="Enter age", example="24")])-> dict:
    return {"message": f"Вы вошли как пользователь {username}, ваш возраст {age}"}