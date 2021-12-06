from fastapi import Request
from typing import Dict, Any, Optional, Union
from fastapi_users import BaseUserManager, InvalidPasswordException
from fastapi_users.jwt import generate_jwt
from ...settings import get_settings
from .auth_schema import UserDB, UserCreate
from ..config_email import get_email_config
from ...apis.stripe.stripe_api import create_stripe_user

settings = get_settings()


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB
    reset_password_token_secret = settings.SECRET
    verification_token_secret = settings.SECRET


    async def on_after_register(self, user: UserDB, request: Optional[Request] = None):
        # token = generate_verification_token(user)
        token = 'test_token'
        # print(f"{settings.URL_NAME}/verify/?token={token}")

        cs = create_stripe_user(user.email)
        print('create stripe customer id: ', cs)
        u1 = await self._update(user, {'stripe_user_id': cs})
        print('u1: -- ', u1)
        u = await self.get(user.id)
        print('get_user: ', u)
        
        auth_str = f"Verification requested for user {user.id}. Verification link: {settings.URL_NAME}/verify-account?token={token}"
        html_email = f"<p>Hello, thank's for your order. You will be invoiced once your order has shipped.</p> <ul> {auth_str} </ul> <br/> {u}"
        await get_email_config(
            _from='Email Verification',
            _recipients=[user.email],
            _subject='Please verify your account.', 
            _email_body=html_email)


    async def on_after_update(self, 
                            user: UserDB, 
                            update_dict: Dict[str, Any], 
                            request: Optional[Request] = None):
        print(f"User {user.id} has been updated with {update_dict}.")

    async def on_after_forgot_password(self, user: UserDB, token: str, request: Optional[Request] = None):
        # Forgot Password (Un-Authenticated User)
        print(f"User {user.id} has forgot their password. Reset token: {token}")  
        link = f'{settings.URL_NAME}/forgot-password-final?q={token}' 
        # auth_str = f"Password reset for user ID: {user.id}, and email: {user.email}. Reset link: http://0.0.0.0:8080/reset?token={token}"
        auth_str = f"Password reset for user {user.email}. Reset link: \n\n {link}"
        html_email = f"<p>Hello!</p> <ul> {auth_str} </ul>"
        await get_email_config(
            _from='Password Reset - SciFi World',
            _recipients=[user.email],
            _subject='Password Reset.', 
            _email_body=html_email)

    async def on_after_reset_password(self, user: UserDB, request: Optional[Request] = None):
        print(f"User {user.id} has reset their password.")




    async def on_after_request_verify(
        self, user: UserDB, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
        print(f"Verification requested for user {user.id}. Verification link: http://0.0.0.0:8000{AUTH_V1_PREFIX}/verify-account?token={token}")

    async def on_after_verify(self, user: UserDB, request: Optional[Request] = None):
        print(f"User {user.id} has been verified")
        # print(f"Verification requested for user {user.id}. Verification link: http://0.0.0.0:8000{AUTH_V1_PREFIX}/verify-account?token={token}")



    async def validate_password(self, password: str, user: Union[UserCreate, UserDB],
    ) -> None:
        if len(password) < settings.MIN_PASSWORD_LEN:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters")

        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters")
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail")
