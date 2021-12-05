from fastapi import FastAPI, Depends, Response, Request
from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import JSONResponse

from fastapi_jwt_auth.exceptions import AuthJWTException

from .routers.v1.stripe import (products)
from .routers.v1.auth import (fastapi_jwt_auth_routes)

from .config.auth.auth_backends import jwt_authentication
from .config.auth.fapi_users import api_users
from .config.config import get_settings
from .config.auth.after_actions import *
from .config.route_prefix import *

settings = get_settings()
SECRET = settings.SECRET
CORS_ORIGINS = settings.CORS_ORIGINS


app = FastAPI(
    openapi_url=settings.OPENAPI_URL,
    docs_url=settings.DOCS_URL, 
    redoc_url=settings.REDOC_URL)

app.add_middleware(CORSMiddleware, 
                   allow_origins=CORS_ORIGINS,
                   allow_credentials=True, 
                   allow_methods=["*"], 
                   allow_headers=["*"])

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})

app.include_router(products.router, 
                    tags=['Stripe'])

app.include_router(fastapi_jwt_auth_routes.router, 
                    prefix='/auth', 
                    tags=['Fastapi JWT Auth'])

# Login
# jwt_auth_router = api_users.get_auth_router(jwt_authentication)
# app.include_router(
#     jwt_auth_router, 
#     prefix="/auth/jwt", 
#     tags=AUTH_TAGS)

# Register
app.include_router(
    api_users.get_register_router(), 
    prefix="/auth", 
    tags=AUTH_TAGS)


'''
Forgot Password and Reset Password
Forget password: for logged-out user
Reset password: for logged-in user'''
app.include_router(
    api_users.get_reset_password_router(),
    prefix="/auth", 
    tags=AUTH_TAGS)

# Manage Users
app.include_router(
    api_users.get_users_router(), 
    prefix="/users", 
    tags=["users"])


# https://frankie567.github.io/fastapi-users/configuration/authentication/jwt/#tip-refresh
# @app.post("/auth/jwt/refresh")
# async def refresh_jwt(response: Response, user=Depends(api_users.current_user())):
#     return await jwt_authentication.get_login_response(user, response)

