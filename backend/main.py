from fastapi import FastAPI, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
# from .routers.v2 import crud_routes
# from .routers.v2.blog import blog_routes
from .routers.v2.stripe import (products)
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

app.include_router(products.router, tags=['Stripe'])


# Register
app.include_router(
    api_users.get_register_router(), 
    prefix="/auth", 
    tags=AUTH_TAGS)


# Login
jwt_auth_router = api_users.get_auth_router(jwt_authentication)
app.include_router(
    jwt_auth_router, 
    prefix="/auth/jwt", 
    tags=AUTH_TAGS)


# Request verify
# request_verification_router = api_users.get_verify_router(
#     SECRET, 
#     after_verification_request=after_verification_request)

# request_verification_router.routes = [route for route in request_verification_router.routes if route.name != "verify"]
# app.include_router(request_verification_router,
#                    prefix="/auth", 
#                    tags=AUTH_TAGS)

# Verify Account
# app.include_router(
#     api_users.get_verify_account(SECRET, 
#                                  after_verification=after_verification_request),
#     prefix='/auth',
#     tags=AUTH_TAGS)

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
@app.post("/auth/jwt/refresh")
async def refresh_jwt(response: Response, user=Depends(api_users.current_user())):
    return await jwt_authentication.get_login_response(user, response)

