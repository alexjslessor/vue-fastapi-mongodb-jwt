from fastapi import (APIRouter, 
                     Depends,
                     Query,
                     HTTPException,
                     status)
from typing import Dict, List, Optional, Tuple
from enum import Enum
from bson import ObjectId, errors
from motor.motor_asyncio import AsyncIOMotorDatabase
from ....config.fastapi_users import fastapi_users
from ....config.config import get_settings
from ....db.schemas import (User, 
                           ReadProduct,
                           ReadShippingAddress,
                           ReadOrder,
                           ReadOrderV2)

from ....db.conn import db, get_database

from ....funcs.json_responses import (exception_400,
                                      error_400,
                                      json_resp_success_200)



async def get_product_by_oid_or_404(id: ObjectId = Depends(get_object_id),
                                    database: AsyncIOMotorDatabase = Depends(get_database),
                                    ) -> ReadProduct:
    
    if (raw_product := await database["Products"].find_one({"_id": id})) is not None:
        return ReadProduct(**raw_product)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


async def get_product_by_sku_or_404(id: str,
                                    database: AsyncIOMotorDatabase = Depends(get_database)
                                    ) -> ReadProduct:
    raw_post = await database["Products"].find_one({"sku": id})
    if raw_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return ReadProduct(**raw_post)

async def get_inventory_by_oid_or_404(id: ObjectId = Depends(get_object_id),
                                database: AsyncIOMotorDatabase = Depends(get_database)
                                ) -> ReadProduct:
    raw_post = await database["Products"].find_one({"_id": id}, {"inventory": 1})
    # raw_post = await database["Products"].find_one({"_id": id})
    if raw_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return ReadProduct(**raw_post)




async def get_shipto_by_oid_or_404(id: ObjectId = Depends(get_object_id),
                                    database: AsyncIOMotorDatabase = Depends(get_database),
                                    ) -> ReadShippingAddress:
    
    if (raw := await database["ShipTo"].find_one({"_id": id})) is not None:
        return ReadShippingAddress(**raw)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)



import asyncio

# https://stackoverflow.com/questions/62176212/how-to-execute-2-coroutines-in-python-3-6
# https://stackoverflow.com/questions/68733675/can-i-use-await-on-multiple-functions-at-once

oid = ''

async def func1():
    raw_order = db["Order"].find({"invoice_num": '1000061'})
    if raw_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    result = [ReadOrder(**i) async for i in raw_order]
    shipto_id = result[0].shipto_ref[0]
    oid = shipto_id
    print('shipto_id: ', shipto_id)
    return result

async def func2():
    shipto_id = '601845ce47ee4245462e07d9'
    raw_shipto = await db["ShipTo"].find_one({'_id': ObjectId(oid=shipto_id)})
    # shipto = [ReadShippingAddress(**i) async for i in raw_shipto]
    # print(raw_shipto)
    return raw_shipto

async def get_order_by_invoice_num_or_404(invoice_num: str,
                                        document: str,
                                        database: AsyncIOMotorDatabase = Depends(get_database)
                                        ):

    # result = await asyncio.gather(*[func1(), func2()])
    # print(result)
    # print('oid: ', oid)


    # tasks = [asyncio.ensure_future(coro()) for coro in (coro1, coro2)]
    tasks = [asyncio.ensure_future(coro()) for coro in (func1, func2)]
    # tasks = [coro(i) for i in range(1, 11)]
    print(tasks)

    # loop = asyncio.get_event_loop()

    # finished, unfinished = loop.run_until_complete(asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED))
    # finished, unfinished = asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # for task in finished:
        # print(task.result())

    return ''


# async def get_order_by_invoice_num_or_404(invoice_num: str,
#                                         document: str,
#                                         database: AsyncIOMotorDatabase = Depends(get_database)
#                                         ):
#     raw_order = database["Order"].find({"invoice_num": invoice_num})
#     if raw_order is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#     result = [ReadOrder(**i) async for i in raw_order]
    
#     shipto_id = result[0].shipto_ref[0]
#     raw_shipto = await database["ShipTo"].find_one({'_id': ObjectId(oid=shipto_id)})
#     # shipto = ReadShippingAddress(**raw_shipto)
#     shipto = [ReadShippingAddress(**i) async for i in raw_shipto]

#     # shipto = await get_shipto_by_oid_or_404(shipto_id)
#     print(shipto)

#     return result
