from starlette.responses import JSONResponse, RedirectResponse, FileResponse
from starlette.requests import Request

from fastapi.encoders import jsonable_encoder

from fastapi import (APIRouter,
                     Depends,
                     BackgroundTasks,
                     HTTPException)

from fastapi import (status,
                     File, 
                     UploadFile, 
                     Form, 
                     Request,
                     Body)

from typing import Optional, List
# from bson import ObjectId
from pydantic import UUID4, BaseModel, EmailStr, Field

from ....config.config import get_settings
# from ....utils import Utils
# from ....apis.deps import *
# from ....db.schemas import User, PostsModel, PyObjectId
from ....config.auth.conn.conn import get_db

from fastapi_jwt_auth import AuthJWT
from motor.motor_asyncio import AsyncIOMotorDatabase
import uuid

router = APIRouter()
settings = get_settings()


class CreateUpdateDictModel(BaseModel):
    def create_update_dict(self):
        return self.dict(
            exclude_unset=True,
            exclude={
                "id",
                "is_superuser",
                "is_active",
                "is_verified",
                "oauth_accounts",
            },
        )

    def create_update_dict_superuser(self):
        return self.dict(exclude_unset=True, exclude={"id"})

class BaseUser(CreateUpdateDictModel):
    # id: UUID4 = Field(default_factory=uuid.uuid4)
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

class User(BaseModel):
# class User(BaseUser):
    # id: UUID4 = Field(default_factory=uuid.uuid4)
    username: str = 'u'
    password: str = 'pass'
    email: EmailStr
    # is_active: bool = True
    # is_superuser: bool = False
    # is_verified: bool = False


# https://indominusbyte.github.io/fastapi-jwt-auth/usage/basic/
@router.post('/jwt/login')
async def login(
    user: User, 
    Authorize: AuthJWT = Depends(),
    db: AsyncIOMotorDatabase = Depends(get_db)):
    
    query = await db["User"].find_one({'email': user.email})

    if query['email'] != user.email:
        raise HTTPException(status_code=401,
                            detail="Bad username or password")

    access_token = Authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}


# @router.post("/refresh")
# def refresh(Authorize: AuthJWT = Depends()):
#     Authorize.jwt_refresh_token_required()

#     current_user = Authorize.get_jwt_subject()
#     new_access_token = Authorize.create_access_token(subject=current_user)

#     Authorize.set_access_cookies(new_access_token)
#     return {"refresh": "successful", "access_token": new_access_token}



# protect endpoint with function jwt_required(), which requires
# a valid access token in the request headers to access.
# @router.get('/user')
# def user(Authorize: AuthJWT = Depends()):
#     Authorize.jwt_required()

#     current_user = Authorize.get_jwt_subject()
#     return {"user": current_user}




# @router.get("/me", response_model=schemas.User)
# def get_user(db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
#     auth_check(Authorize)
#     auth_setting = str(settings.DISABLE_AUTH)
#     if auth_setting.lower() == "true":
#         current_user = schemas.User
#         current_user.authDisabled = True
#         current_user.id = 0
#         current_user.username = "user"
#         current_user.is_active = True
#         current_user.is_superuser = True
#         return current_user
#     else:
#         Authorize.jwt_required()
#         current_user = Authorize.get_jwt_subject()
#         if current_user is not None:
#             return crud.get_user_by_name(db=db, username=current_user)
#         else:
#             raise HTTPException(status_code=401, detail="Not logged in.")


# @router.post("/me", response_model=schemas.User)
# def update_user(
#     user: schemas.UserCreate,
#     db: Session = Depends(get_db),
#     Authorize: AuthJWT = Depends(),
# ):
#     auth_check(Authorize)
#     current_user = Authorize.get_jwt_subject()
#     return crud.update_user(db=db, user=user, current_user=current_user)


# @router.get("/logout")
# def logout(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
#     auth_check(Authorize)
#     crud.blacklist_login_token(Authorize, db)
#     return {"msg": "Logout Successful"}


# @router.get("/logout/refresh")
# def logout(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
#     Authorize.jwt_refresh_token_required()
#     Authorize.unset_jwt_cookies()
#     crud.blacklist_login_token(Authorize, db)
#     return {"msg": "Logout Successful"}
