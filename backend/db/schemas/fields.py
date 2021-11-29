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
from pydantic import  BaseModel, Field, validator, EmailStr, root_validator
from datetime import datetime, timezone
from bson import ObjectId
import base64


# settings = get_settings()


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

    def __repr__(self):
        return f'OID({super().__repr__()})'
