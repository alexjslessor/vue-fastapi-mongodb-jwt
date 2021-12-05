from fastapi import (APIRouter, 
                     Depends,
                     Query,
                     HTTPException,
                     status,
                     Request)
from typing import Dict, List, Optional, Tuple
from enum import Enum
from bson import ObjectId, errors
from motor.motor_asyncio import AsyncIOMotorDatabase

from ....utils import *
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
from .crud_funcs import *
# import requests

settings = get_settings()
router = APIRouter()
dd = DocData()
basedir = os.path.abspath(os.path.dirname('static'))



@router.get("/{invoice_num}/doc/{document}.pdf")
async def print_pdf(order: ReadOrder = Depends(get_order_by_invoice_num_or_404)):
    print(order)
    return ''

# @router.get("/{invoice_num}/doc/{document}.pdf")
# async def print_pdf(invoice_num: str, 
#                     document: str):

    # query = db["Order"].find({'invoice_num': invoice_num})
    # result = [ReadOrder(**raw_order) async for raw_order in query]

    # shipto_id = result[0].shipto_ref[0]
    # shipto_id = '601845ce47ee4245462e07d9'

    # if not ObjectId.is_valid(shipto_id):
        # return exception_400(settings.OID_ERROR, 'red')

    # shipto = requests.get(f'http://127.0.0.1:5000/read/single_shipto/{shipto_id}')
    # shipto = await db["ShipTo"].find_one({'_id': ObjectId(oid=shipto_id)})
    # shipto = [ReadShippingAddress(**addr) async for addr in query_shipto]

    # if (p := db["ShipTo"].find_one({"_id": shipto_id})) is not None:
        # print(p)
    # print(result)
    # print('--' *22)
    # df = create_invoice_table(result)
    # print(df)
    # print('--' *22)
    # print(shipto)
    # print(d)

    # item_table = df.to_html(index=False, decimal='.', float_format='%.2f')
    # total_price = '{0:.2f}'.format(df['Sub Total'].sum())
    
    # data = dd.invoice_template(dd.from_name,
    #                            dd.from_street, 
    #                            to_name,
    #                            to_street,
    #                            invoice_num,
    #                            dd.todays_date,
    #                            item_table,
    #                            total_price)
    
    # css = CSS(filename=os.path.join(basedir, 'static/report_styles/invoice_weasyprint.css'))
    # file_name = f'{invoice_num}-{document}.pdf'
    
    # html = HTML(string=data).write_pdf(file_name, stylesheets=[css])
    # file_path = str(os.path.join(basedir, file_name))
    # return exception_400(settings.READ_ALL_PROD_ERR, 'red')

    # return ''


class AllProductPath(str, Enum):
    '''These are same values as in constants.js on frontend'''
    active_and_inactive = 'allProducts'
    active_products = "isActive"


@router.get("/read/all_products/{filter_by}",
            response_description="List all products", 
            response_model=List[ReadProduct])
async def all_products(
    filter_by: AllProductPath,
    pagination: Tuple[int, int] = Depends(pagination),
    database: AsyncIOMotorDatabase = Depends(get_database),
    current_user: User = Depends(fastapi_users.current_user())
    ) -> List[ReadProduct]:
    
    skip, limit = pagination

    if filter_by.value == 'isActive':
        query = database["Products"].find({'is_active': '1'}, skip=skip, limit=limit)
        results = [ReadProduct(**raw_post) async for raw_post in query]
        print(f'list_products: {filter_by.value} ')
        return results

    if filter_by.value == 'allProducts':
        query = database["Products"].find({}, skip=skip, limit=limit)
        results = [ReadProduct(**raw_post) async for raw_post in query]
        print('list_products: ')
        return results

    return exception_400(settings.READ_ALL_PROD_ERR, 'red')

# @router.get("/read/all_products")
# async def all_products(
#     pagination: Tuple[int, int] = Depends(pagination),
#     database: AsyncIOMotorDatabase = Depends(get_database)) -> List[ReadProduct]:
#     skip, limit = pagination
#     query = database["Products"].find({}, skip=skip, limit=limit)
#     results = [ReadProduct(**raw_post) async for raw_post in query]
#     print('list_products: ', results)
#     return results

# @router.get("/read/all_products", 
            # response_description="List all products", 
            # response_model=List[ReadProduct])
# async def all_products(
#     limit: Optional[int] = Query(1000, alias="limit", title='Limit Results.', description='Limit Results', example='100'),
#     is_active: Optional[int] = Query(None, alias='isActive', title='Active Product', description='Active Product', example='1 or 0'),
#     current_user: User = Depends(fastapi_users.current_user())):

#     if is_active:
#         p = await db["Products"].find({'is_active': f'{is_active}'}).to_list(limit)
#         if len(p) > 0:
#             return p
#         else:
#             return exception_400(settings.READ_ALL_PROD_ERR, 'red')
    
#     p = await db["Products"].find({}).to_list(limit)
#     if len(p) > 0:
#         return p

#     return exception_400(
#         settings.READ_ALL_PROD_ERR, 'red')




@router.get("/read/single_product/inventory/{id}", 
            response_model=ReadProduct)
async def single_product_inventory_by_oid(
    product: ReadProduct = Depends(get_inventory_by_oid_or_404)
    ) -> ReadProduct:
    return product

@router.get("/read/single_product/{id}", 
            response_description="Get a single product", 
            response_model=ReadProduct)
async def get_product_by_sku(product: ReadProduct = Depends(get_product_by_sku_or_404)) -> ReadProduct:
    return product

# @router.get("/read/single_product/{id}", 
#             response_description="Get a single product", 
#             response_model=ReadProduct)
# async def get_product_by_id(product: ReadProduct = Depends(get_product_by_oid_or_404)) -> ReadProduct:
#     return product


# @router.get("/read/single_product/{id}", response_description="Get a single product", 
#             response_model=ReadProduct)
# async def single_product(id: str,
#                          current_user: User = Depends(fastapi_users.current_user())):
#     '''Query by sku '''
#     if (p := await db["Products"].find_one({"sku": id})) is not None:
#         return p

#     return exception_400(settings.READ_SINGLE_PROD_ERR, 'red')








@router.get("/read/single_shipto/{id}", 
            response_description="Read a single shipping address", 
            response_model=ReadShippingAddress)
async def single_shipto(id: str, 
                        current_user: User = Depends(fastapi_users.current_user())):
    '''Query by _id aka id '''
    if not ObjectId.is_valid(id):
        return exception_400(settings.OID_ERROR, 'red')

    if (p := await db["ShipTo"].find_one({"_id": ObjectId(id)})) is not None:
        return p

    return exception_400(
        settings.READ_SINGLE_SHIPTO_ERR, 
        'red')


@router.get("/read/all_shipto", 
            response_description="Read all shipping addresses")
async def list_shipto(pagination: Tuple[int, int] = Depends(pagination),
                    database: AsyncIOMotorDatabase = Depends(get_database)
                    ) -> List[ReadShippingAddress]:
    skip, limit = pagination
    query = database["ShipTo"].find({}, skip=skip, limit=limit)
    results = [ReadShippingAddress(**raw_addr) async for raw_addr in query]
    # print('list_shipto: ', results)
    return results









@router.get("/read/all_orders/{id}", response_model=List[ReadOrder])
async def all_orders(id: str,
                    current_user: User = Depends(fastapi_users.current_user())
                    ):
    lst = []
    for d in await db['Order'].find(
        {
            'product_id': ObjectId(id),
            'status': {'$nin': ['Cancelled', 'Complete', 'Reconcile', 'Shipped']}
            # 'status': {'$in': ['Pending', 'In Production', 'Acknowledged', 'Back-Ordered']}
        }).to_list(1000):
        # print('d: ', d)
        lst.append(d)
    return lst

# async def get_user_order_or_404(current_user: User = Depends(fastapi_users.current_user()),
#                                 database: AsyncIOMotorDatabase = Depends(get_database)
#                                 ) -> NewReadOrder:
    
#     if (raw_order := await database["Orders"].find_one({"user_id": current_user.id})) is not None:
#         return NewReadOrder(**raw_order)
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

# @router.get("/read/all_orders", 
#             response_description="Get a single product", 
#             response_model=NewReadOrder)
# async def get_user_order(order: NewReadOrder = Depends(get_user_order_or_404)):
#     print(order)
#     return order


@router.get("/read/user_order", 
            response_description="Read user order")
async def read_user_order(
                    pagination: Tuple[int, int] = Depends(pagination),
                    database: AsyncIOMotorDatabase = Depends(get_database),
                    current_user: User = Depends(fastapi_users.current_user())):
    skip, limit = pagination
    query = database["Order"].find({"user_id": current_user.id})
    # results = [NewReadOrder(**raw_addr) async for raw_addr in query]
    return NewReadOrder(query)
    print('new orders: ', query)
    return query




