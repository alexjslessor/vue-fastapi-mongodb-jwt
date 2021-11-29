from fastapi.testclient import TestClient
from backend.main import app
from backend.routers.auth import UserDB, User
from backend import models_pydantic as pm
from fastapi_users.password import get_password_hash
from backend.config import _Settings
import pytest
from fastapi.encoders import jsonable_encoder
from uuid import UUID
from os import environ

user_email = environ.get('USERNAME_TEST')
user_password = environ.get('PASSWORD_TEST')
password_hash = get_password_hash(user_password)


@pytest.fixture
def user() -> UserDB:
    return UserDB(
        id=UUID('39ba595e-4d52-43a7-bddc-b9dfc2be50ce'), 
        email=user_email,
        is_active=True, 
        is_superuser=False, 
        hashed_password='z1f2sHntPf.Yt/l631toOgzuppDo3oc4YZbPHjZD.Xox1Lha/EGi', 
        is_first_login=False)

@pytest.fixture
def logged_in_client():
    data={'username': user_email,
          'password': user_password} 
    _client = client.post("/auth/cookie/login", 
                           data=data)
    return _client
