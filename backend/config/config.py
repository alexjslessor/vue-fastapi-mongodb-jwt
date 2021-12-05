import functools
from pydantic import BaseSettings, AnyUrl, BaseModel
from os import environ
from typing import List

'''
setting env vars
https://cloud.google.com/run/docs/configuring/environment-variables
'''

class _BaseSettings(BaseSettings):
    PORT: int = 8080
    SECRET: str = str(environ.get('SECRET'))

    USER_COLLECTION_NAME = 'User'
    MIN_PASSWORD_LEN = 4
    
    MAIL_PORT = 465
    MAIL_SERVER = 'in-v3.mailjet.com'
    MAIL_TLS = False
    MAIL_SSL = True    
    MAILJET_SENDER = 'atom@comrom.ca'
    
    GCP_PROJECT: str = str(environ.get('GCP_PROJECT', 'hi-app-281315'))
    GCP_BUCKET: str = str(environ.get('GCP_BUCKET', 'asd-fastapi'))
    K_SERVICE_ENV: str = str(environ.get('K_SERVICE', 'local'))

    OPENAPI_URL: str = '/docs_openapi'
    DOCS_URL: str = '/docs'
    REDOC_URL: str = '/redoc_url'
    

class DevSettings(_BaseSettings):

    CORS_ORIGINS: List[str] = [
        'http://0.0.0.0:8080',
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:8080/#/",
        'https://fastapi-vue.netlify.app',
        'http://scifi-world.net',
        'https://scifi-world.net',
        'http://192.168.2.21:8080',
        'https://fastapi-vue-mongodb-auth.vercel.app']


    STRIPE_PUBLIC_ALEXJSLESSOR: str = environ.get('STRIPE_PUBLIC_ALEXJSLESSOR')
    STRIPE_SECRET_ALEXJSLESSOR: str = environ.get('STRIPE_SECRET_ALEXJSLESSOR')
    # testing mailjet email creds
    MAIL_USERNAME: str = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD: str = environ.get('MAIL_PASSWORD')
    
    
    MAIL_QUE_SUBJECT = "Hey There!"
    MAIL_DEFAULT_SENDER = 'aslessor@commercialoil.ca'
    MAIL_FROM_NAME = "Alex J Slessor"


    # this does not work locally
    # URL_NAME = 'http://0.0.0.0:8080'
    # this works locally
    # URL_NAME = 'http://localhost:8080'
    # URL_NAME = 'https://scifi-world.net'
    # SET URL_NAME as serverless env variable in cloud
    URL_NAME: AnyUrl = str(environ.get('URL_NAME', 'http://localhost:8080'))


    DATABASE_URL: str = str(environ.get('DATABASE_URL'))
    DB_NAME: str = 'ecomStore'

@functools.lru_cache()
def get_settings(**kwargs) -> BaseSettings:
    return DevSettings(**kwargs)


class jwtSettings(BaseModel):
    authjwt_secret_key: str = str(environ.get('SECRET'))
    # authjwt_secret_key: str = generate_secret_key(db=SessionLocal())
    # authjwt_token_location: set = {"headers", "cookies"}
    # authjwt_cookie_secure: bool = False
    # authjwt_cookie_csrf_protect: bool = True
    # authjwt_access_token_expires: int = int(settings.ACCESS_TOKEN_EXPIRES)
    # authjwt_refresh_token_expires: int = int(settings.REFRESH_TOKEN_EXPIRES)
    # authjwt_cookie_samesite: str = settings.SAME_SITE_COOKIES
    # authjwt_denylist_enabled: bool = True
    # authjwt_denylist_token_checks: set = {"access", "refresh"}


from fastapi_jwt_auth import AuthJWT

@AuthJWT.load_config
def get_config():
    return jwtSettings()


