from fastapi_users import FastAPIUsers
from .auth_backends import auth_backends
from .auth_schema import UserCreate, User, UserDB, UserUpdate
from .conn.conn import get_user_manager


api_users = FastAPIUsers(
    get_user_manager,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB)