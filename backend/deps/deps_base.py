from fastapi import (APIRouter, 
                     Depends,
                     Query,
                     HTTPException,
                     status)
from typing import Dict, List, Optional, Tuple
from enum import Enum
from bson import ObjectId, errors
from motor.motor_asyncio import AsyncIOMotorDatabase

async def pagination(skip: int = Query(0, ge=0),
                    limit: int = Query(0, ge=0)) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


async def get_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except (errors.InvalidId, TypeError):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
