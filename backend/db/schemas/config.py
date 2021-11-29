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

class CreateConfig(BaseModel):
    allow_population_by_field_name = True
    arbitrary_types_allowed = True
    json_encoders = {
        ObjectId: str,
        # ObjectId: lambda oid: str(oid),
    }


class UpdateConfig(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
