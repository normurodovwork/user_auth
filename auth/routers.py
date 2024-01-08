import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from sqlalchemy import Integer

from auth.manager import get_user_manager

from auth.auth import auth_backend
from database import User

fastapi_users = FastAPIUsers[User, Integer](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)