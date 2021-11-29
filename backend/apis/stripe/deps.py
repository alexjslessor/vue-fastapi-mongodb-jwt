import stripe
from enum import Enum
from pprint import pprint
from json import loads, dumps
from fastapi import Depends
from ...config.config import get_settings


settings = get_settings()
stripe.api_key = settings.STRIPE_SECRET_ALEXJSLESSOR


# async def get_user_by_uid_or_404(id: ObjectId = Depends(get_object_id),
#                                     database: AsyncIOMotorDatabase = Depends(get_database),
#                                     ) -> ReadProduct:
    
#     if (raw_product := await database["User"].find_one({"_id": id})) is not None:
#         return ReadProduct(**raw_product)
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


# async def pagination(skip: int = Query(0, ge=0),
#                     limit: int = Query(0, ge=0)) -> Tuple[int, int]:
#     capped_limit = min(100, limit)
#     return (skip, capped_limit)


# async def get_object_id(id: str) -> ObjectId:
#     try:
#         return ObjectId(id)
#     except (errors.InvalidId, TypeError):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


# async def get_product_by_oid_or_404(id: ObjectId = Depends(get_object_id),
#                                     database: AsyncIOMotorDatabase = Depends(get_database),
#                                     ) -> ReadProduct:
    
#     if (raw_product := await database["Products"].find_one({"_id": id})) is not None:
#         return ReadProduct(**raw_product)
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


# async def get_product_by_sku_or_404(id: str,
#                                     database: AsyncIOMotorDatabase = Depends(get_database)
#                                     ) -> ReadProduct:
#     raw_post = await database["Products"].find_one({"sku": id})
#     if raw_post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     return ReadProduct(**raw_post)

# async def get_inventory_by_oid_or_404(id: ObjectId = Depends(get_object_id),
#                                 database: AsyncIOMotorDatabase = Depends(get_database)
#                                 ) -> ReadProduct:
#     raw_post = await database["Products"].find_one({"_id": id}, {"inventory": 1})
#     # raw_post = await database["Products"].find_one({"_id": id})
#     if raw_post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     return ReadProduct(**raw_post)



def stripe_to_json(data):
    a = dumps(data)
    return loads(a)

def create_stripe_user(user_email):
    '''
    https://stripe.com/docs/billing/customer
    https://stripe.com/docs/api/customers/create'''
    c = stripe.Customer.create(email=user_email, 
                            #    payment_method='pm_1FWS6ZClCIKljWvsVCvkdyWg', 
                            #    invoice_settings={'default_payment_method': 'pm_1FWS6ZClCIKljWvsVCvkdyWg'}
                               )

def calculate_order_total(items):
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    total = 0
    for i in items:
        total += i['subtotal']
    return total

def get_all_products(**kwargs):
    # https://stripe.com/docs/api/products/retrieve?lang=python
    p = stripe.Product.list(**kwargs)
    lst = []
    for a in p['data']:
        lst.append(a)
    return lst

def get_subscriptions():
    price = stripe.Price.list()
    product = stripe.Product.list()
    l = [{'product_id': pro['id'],
         'product_img': pro['images'][0],
         'product_name': pro['name'],
         'product_description': pro['description'],
         'price_id': pri['id'],
         'price': pri['unit_amount'],
         'quantity': 0,
         'subtotal': 0.00} for pro in product['data'] for pri in price['data'] if pri['product'] == pro['id'] if 'is_subscription' in pro['metadata']]
    return l


def modify_product(pid, **kwargs):
    # https://stripe.com/docs/api/products/update
    stripe.Product.modify(pid, **kwargs)


def get_product_by_id(prod_id='prod_JI9Ojis5hR4qSW'):
    price = stripe.Price.list()
    product = stripe.Product.retrieve(prod_id)
    d = {}
    for _price in price['data']:
        if _price['product'] == prod_id:
            d['product_id'] = prod_id
            d['product_img'] = product['images']
            d['product_name'] = product['name']
            d['product_description'] = product['description']
            d['price_id'] = _price['id']
            d['price'] = _price['unit_amount']   
            d['quantity'] = 0
            d['subtotal'] = 0.00     
    # print(d)
    return d

def join_all_products_prices():
    price = (stripe.Price.list()).get('data')
    product = (stripe.Product.list()).get('data')
    
    lst = [{'product_id': _product['id'],
        'product_img': _product['images'],
        'product_name': _product['name'],
        'product_description': _product['description'],
        'price_id': _price['id'],
        'price': _price['unit_amount'],
        'quantity': 0,
        'subtotal': 0.00} \
            for _product in product for _price in price \
                if _price['product'] == _product['id']]
    return lst



if __name__ == "__main__":
    p = join_all_products_prices()
    # p = get_product_by_id()
    pprint(p)
    