# from fastapi import status, HTTPException
# from fastapi_users import FastAPIUsers
# from fastapi_users.models import BaseUserCreate, BaseUserDB
# from fastapi_users.user import CreateUserProtocol
# from .auth_schema import UserCreate
# from typing import cast


# def get_create_user(old_create_user: CreateUserProtocol) -> CreateUserProtocol:
#     '''https://github.com/frankie567/fastapi-users/discussions/598'''
#     async def create_user(user: BaseUserCreate,
#                           safe: bool = False,
#                           is_active: bool = None,
#                           is_verified: bool = None) -> BaseUserDB:
        
#         existing_user = None
#         try:# new_user is form data from app
#             new_user = cast(UserCreate, user)
#             # print('new_user: ', user)
#             existing_user = await fastapi_users.get_user(new_user.email)
#             # print('existing_user: ', existing_user)
#         except Exception as e:
#             print(e)

#         if existing_user:
#             if new_user.email == existing_user.email:
#                 raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                                     detail='Username already in use, please choose another')
#         return await old_create_user(user, safe, is_active, is_verified)
#     return create_user


# class FastAPIUsersOverride(FastAPIUsers):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.create_user = get_create_user(self.create_user)

# # from fastapi_users.router.verify import VERIFY_USER_TOKEN_AUDIENCE
# # from fastapi_users.utils import generate_jwt
# # https://github.com/frankie567/fastapi-users/discussions/604
# # def generate_verification_token(user: UserDB) -> str:
# #     token_data = {
# #         "user_id": str(user.id),
# #         "email": str(user.email),
# #         "aud": VERIFY_USER_TOKEN_AUDIENCE}

# #     token = generate_jwt(
# #         token_data,
# #         settings.VERIFICATION_SECRET,
# #         3600)
# #     return token
