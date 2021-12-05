from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import (APIRouter, 
                     Depends, 
                     status,
                     Body)
from ....config.fastapi_users import fastapi_users
from ....config.config import get_settings
from ....db.schemas import (User, 
                           CreateProduct,
                           CreateShippingAddress,
                           CreateOrder,
                           PydanticModels as pm)
from ....db.conn import db, get_database
from ....funcs.json_responses import (exception_400,
                                      error_400,
                                      json_resp_success_200)
router = APIRouter()
'''
Creates new records:
Products
ShipTo
'''
@router.post("/create_product")
async def create_product(newProduct: CreateProduct = Body(...),
                        current_user: User = Depends(fastapi_users.current_user())
                        ):
    
    json_encoded = jsonable_encoder(newProduct)
    print(json_encoded)

    # new_prod = await db["Products"].update_one({'sku', json_encoded['sku']}, json_encoded)
    new_prod = await db["Products"].insert_one(json_encoded)
    if new_prod.acknowledged:
        return json_resp_success_200('Product Created.', 'green')

    else:
        return exception_400('Error: 400.', 'red')

@router.post("/create_shipto")
async def create_shipto(newShipto: CreateShippingAddress = Body(...),
                        current_user: User = Depends(fastapi_users.current_user())
                        ):
    json_encoded = jsonable_encoder(newShipto)
    print(json_encoded)
    
    new_shipto = await db["ShipTo"].insert_one(json_encoded)    
    if new_shipto.acknowledged:
        return json_resp_success_200('Customer Shipping Address Created', 'green')
    
    else:
        return exception_400('Address Creation Error', 'red')



@router.post("/create/create_order", 
# response_model=CreateOrder
)
async def create_order(createOrder: CreateOrder = Body(...),
                        current_user: User = Depends(fastapi_users.current_user())
                        ):
    # print('user: ', current_user.id)
    json_encoded = jsonable_encoder(createOrder)
    json_encoded.update({'user_id': current_user.id})
    print(json_encoded)

    new_order = await db["Order"].insert_one(json_encoded)    
    if new_order.acknowledged:
        return json_resp_success_200('Order Created', 'green')    
    else:
        return exception_400('Order Creation Error', 'red')

    # print(json_encoded)
    # new_order = PostDB(**order.dict())
    # await database["posts"].insert_one(post_db.dict(by_alias=True))
    # post_db = await get_post_or_404(post_db.id, database)
    # return new_order
    # return ''