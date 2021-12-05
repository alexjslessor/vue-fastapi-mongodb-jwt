from fastapi.encoders import jsonable_encoder
from fastapi import (APIRouter, 
                     Depends, 
                     Body,
                     status,
                     HTTPException)
from bson import ObjectId
from ....config.fastapi_users import fastapi_users
from ....config.config import get_settings
from ....db.conn import db
from ....db.schemas import (User, 
                           UpdateProduct,
                           UpdateShipto,
                           UpdateOrder)
from ....funcs.json_responses import (exception_400,
                                      error_400,
                                      json_resp_success_200)
settings = get_settings()
router = APIRouter()
'''
https://github.com/tiangolo/fastapi/issues/1515
Updates collection data:
Products
ShipTo
'''
@router.post("/update_product/{id}")
async def update_product(id: str, 
                         updateProduct: UpdateProduct = Body(...),
                         current_user: User = Depends(fastapi_users.current_user())):

    if not ObjectId.is_valid(id):
        return exception_400(settings.OID_ERROR, 
                             'red')

    product = {k: v for k, v in updateProduct.dict().items() if v is not None} 
    # print('product: ', product)   
    if len(product) >= 1:
        update_result = await db["Products"].update_one({"_id": ObjectId(oid=id)}, 
                                                        {"$set": product})
        # https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.UpdateResult
        if update_result.modified_count == 1:
            return json_resp_success_200(f'Product Updated.', 
                                         'green')
        else:
            return json_resp_success_200('No Changes Applied.', 'yellow')

    return exception_400('Error: 400.', 
                         'red')


@router.post("/update_shipto/{id}")
async def update_shipto(id: str, 
                        updateShipto: UpdateShipto = Body(...),
                        current_user: User = Depends(fastapi_users.current_user())
                        ):

    if not ObjectId.is_valid(id):
        return exception_400(settings.OID_ERROR, 
                         'red')

    shipto = {k: v for k, v in updateShipto.dict().items() if v is not None}  
    # print('shipto: ', shipto)

    if len(shipto) >= 1:
        update_result = await db["ShipTo"].update_one({"_id": ObjectId(oid=id)}, 
                                                      {"$set": shipto})
        if update_result.modified_count == 1:
            return json_resp_success_200('Shipping Address Updated.', 
                                         'green')
        else:
            return json_resp_success_200('No Changes Applied.', 
                                         'yellow')  
    else:
        return exception_400('Error: 400.', 'red')


# from pprint import pprint

@router.post("/update_order/{id}")
async def update_order(id: str, 
                       updateOrder: UpdateOrder = Body(...),
                       current_user: User = Depends(fastapi_users.current_user())):

    if not ObjectId.is_valid(id):
        return exception_400(settings.OID_ERROR, 'red')

    order = {k: v for k, v in updateOrder.dict().items() if v is not None}    
    print('order: ', order)

    if len(order) >= 1:
        update_result = await db["Order"].update_one({"_id": ObjectId(oid=id)}, 
                                                    {"$set": order })
        if update_result.modified_count == 1:
            return json_resp_success_200(f"Order {order['order_sku']} Updated.", 'green')
        else:
            return json_resp_success_200('No Changes Applied.', 'yellow')  
    else:
        return exception_400('Error: 400.', 'red')