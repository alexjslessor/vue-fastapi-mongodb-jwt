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
from fastapi.responses import JSONResponse
from pydantic import  BaseModel, Field, validator, EmailStr, root_validator
from datetime import datetime, timezone
from bson import ObjectId
import base64
from ..fields import PyObjectId
from ..config import *
from .stripe_enum import *

# settings = get_settings()
  
class PostsModel(CreateConfig):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    headline: str = Field(...)
    post_image_bytes: bytes = Field(...)
    post_image_content_type: str = Field(...)
    content: str = Field(...)



class UpdatePostModel(UpdateConfig):
    title: Optional[str]
    headline: Optional[str]
    post_image_bytes: Optional[str]
    post_image_content_type: Optional[str]
    content: Optional[str]