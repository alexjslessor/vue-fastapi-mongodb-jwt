# from pydantic import root_validator
# from pydantic import validator, EmailStr, root_validator
# from fastapi_users.password import verify_and_update_password
from pydantic import BaseModel, validator
from datetime import datetime, timezone
from fastapi import status, HTTPException
from ..config import get_settings

settings = get_settings()


# @validator('email')
def validate_email(cls, v: str):
    print('validate user register: ', v)
    return v

def validate_password(cls, v: str):        
    '''https://pydantic-docs.helpmanual.io/usage/validators/'''
    if len(v) < settings.MIN_PASSWORD_LEN:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail=f"Password must be a minimum of {settings.MIN_PASSWORD_LEN} characters in length.")
    return v


def always_update_last_updated(cls, v):
    return datetime.now()

'''https://github.com/frankie567/fastapi-users/discussions/587'''
def doc_created_at(v):
    return v or datetime.now(timezone.utc)

