from typing import Dict, Any, Optional, cast, List
from enum import Enum
from fastapi import (status,
                     File, 
                     UploadFile, 
                     Form, 
                     Request,
                     Body,
                     status, 
                     HTTPException)
from fastapi_users.password import verify_and_update_password
from fastapi_users.models import BaseUserCreate, BaseUserDB, BaseUserUpdate, BaseUser
from fastapi_users.models import BaseUserCreate
from fastapi.responses import JSONResponse
# from .auth_utils.override import FastAPIUsersOverride

from pydantic import  BaseModel, Field, validator, EmailStr, root_validator
from datetime import datetime, timezone
from ..config import get_settings
from .validators import *
from bson import ObjectId
import base64

settings = get_settings()


class User(BaseUser):
    '''user_model: Pydantic model of a user.'''
    '''BaseUser: provides the basic fields and validation'''
    is_first_login: Optional[bool] = False
    created_at: datetime = None
    stripe_user_id: str = None

    _default_created_at = validator('created_at', pre=True, always=True, allow_reuse=True)(doc_created_at)

class UserDB(User, BaseUserDB):
    '''user_db_model: Pydantic model of a DB representation of a user.'''
    '''BaseUserDB: is a representation of the user in database, adding a hashed_password field'''
    is_first_login: Optional[bool] = False
    created_at: datetime = None
    stripe_user_id: str = None

class UserCreate(BaseUserCreate):
    '''user_create_model: Pydantic model for creating a user.'''
    '''BaseCreateUser: dedicated to user registration, consists of compulsory email and password fields'''
    is_first_login: Optional[bool] = False
    created_at: datetime = None
    stripe_user_id: str = None

    _email = validator('email', pre=True, always=True, allow_reuse=True)(validate_email)



class UserUpdate(User, BaseUserUpdate):
    '''user_update_model: Pydantic model for updating a user.'''
    '''BaseUpdateUser: dedicated to user profile update, adds an optional password field'''
    pass




