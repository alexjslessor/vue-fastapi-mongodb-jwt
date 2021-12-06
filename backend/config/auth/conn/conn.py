from fastapi_users.db import MongoDBUserDatabase
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import Depends
from ....settings import get_settings
from ..auth_schema import UserDB
from ..after_actions import UserManager
from pymongo.errors import ServerSelectionTimeoutError

try:
    settings = get_settings()
except ServerSelectionTimeoutError as e:
    raise 'MongoDB Connection Error'
    
DB_URL = settings.DATABASE_URL
DB_NAME = settings.DB_NAME
USER_COLLECTION = settings.USER_COLLECTION_NAME

client = AsyncIOMotorClient(DB_URL, uuidRepresentation="standard")

db = client[DB_NAME]
collection = db[USER_COLLECTION]

user_db = MongoDBUserDatabase(UserDB, collection)

def get_db() -> AsyncIOMotorDatabase:
    return db

def get_user_db():
    yield MongoDBUserDatabase(UserDB, collection)

def get_user_manager(user_db: MongoDBUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
