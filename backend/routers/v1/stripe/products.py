from fastapi import (APIRouter,
                     Depends,
                     BackgroundTasks,
                     HTTPException,
                     status,
                     File, 
                     UploadFile, 
                     Form,
                     Body)

from fastapi.responses import RedirectResponse, FileResponse, JSONResponse
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi.encoders import jsonable_encoder
from typing import Optional, List, Dict
import stripe


from ....config.auth.auth_schema import User
from ....config.auth.fapi_users import api_users
from ....config.auth.conn.conn import (
    get_user_manager, 
    get_db, 
    get_user_db)

from ....db.schemas.stripe.stripe_enum import *
from ....db.schemas.stripe.stripe_schema import (
    PydanticModels as pm, 
    UpdateStripeProductModel as uspm)

# from ....config.config import get_settings
from ....settings import get_settings

from ....apis.stripe.deps import *

router = APIRouter()
settings = get_settings()
stripe.api_key = settings.STRIPE_SECRET_ALEXJSLESSOR


@router.post("/ecom/update_db/{id}", response_model=uspm)
async def update_product(id: str, product: uspm = Body(...)):
    
    new_product = {k: v for k, v in product.dict().items() if v is not None}
    if len(new_product) >= 1:
        stripe_product = stripe.Product.retrieve(id)
        stripe_product_img_lst = stripe_product.images
    
        if new_product.get('images'):
            filter_duplicate_images = list(set(stripe_product_img_lst + new_product['images']))
            modify_product(id, images=filter_duplicate_images)
            return JSONResponse(status_code=status.HTTP_200_OK, 
                                content='Product Images Updated')
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Product {id} not found")


@router.post("/user/after_create")
async def after_user_create(
    db: AsyncIOMotorDatabase = Depends(get_db),
    current_user: User = Depends(api_users.current_user())
    ):
    print(db)
    print(current_user)

    return JSONResponse(status_code=status.HTTP_200_OK, 
                        content='Smash')


# @router.get("/read/single_product/{id}", 
#             response_description="Get a single product", 
#             response_model=ReadProduct)
# async def get_product_by_sku(product: ReadProduct = Depends(get_product_by_sku_or_404)) -> ReadProduct:
#     return product

@router.get("/read/stripe/product/all", 
            response_description="Read all stripe products")
async def read_all_stripe_products(
    # products = Depends(read_stripe_products),
    ):
    p = join_all_products_prices()
    return stripe_to_json(p)
    # return products


@router.get("/query_db/{query}/{filter}")
async def query_db(query: ProductModel, 
                   filter: Optional[str] = None,
                #    current_user: User = Depends(api_users.current_user())
                   ):

    if query == ProductModel.all_products:
        p = join_all_products_prices()
        # print(p)
        return stripe_to_json(p)


    if query == ProductModel.all_mongo_products:
        v = Vendor.objects.only('products')
        q = v.to_json()
        return loads(q)

    if query == ProductModel.single_product:
        # p = get_single_product(filter)
        p = get_product_by_id(filter)
        return stripe_to_json(p)

    if query == ProductModel.subscriptions:
        p = get_subscriptions()
        return stripe_to_json(p)
    
    return JSONResponse(status_code=status.HTTP_200_OK, 
                        content=query)


@router.post("/cart-checkout")
def cart_checkout_session(cart: pm.GetCheckout):
    cart_items = cart.cart_items['cart']
    customer_info = cart.cart_items['info']
    
    print('cart items: ', cart_items)
    print('--'*40)
    print('customer info: ', customer_info)
    
    # line_items = [{'price': a['priceId'], 
    #    'quantity': a['quantity']} for a in cart_items]

    # total = calculate_order_total(cart_items)
    # intent = stripe.PaymentIntent.create(
        # receipt_email=customer_info.get('email')
        # amount=total, 
        # currency='cad', 
        # payment_method_types=['card'])
    # print('intent: ', intent)
    # return {'clientSecret': intent['client_secret']}
    return ''
    # session = stripe.checkout.Session.create(
    #   success_url='http://localhost:8080/success',
    #   cancel_url="http://localhost:8080",
    #   payment_method_types=["card"],
    #   line_items=line_items,
    #   mode="payment")
    # return {'id': session.id}


@router.post("/create-checkout-session")
def create_checkout_session():
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://localhost:8080/success',
    cancel_url='http://localhost:8080/')
  return {'id': session.id}




# https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#redirect
# @app.route('/create-customer-portal-session', methods=['POST'])
# def customer_portal():
#   # Authenticate your user.
#   session = stripe.billing_portal.Session.create(
#     customer='{{ CUSTOMER_ID }}',
#     return_url='https://example.com/account',
#   )
#   return redirect(session.url)


# @router.get("/read/product/{query}/{filter}")
# async def read_single_product(query: ProductModel, 
#                    filter: Optional[str] = None,
#                    current_user: User = Depends(api_users.current_user())):

#     if query == ProductModel.single_product:
#         # p = get_single_product(filter)
#         p = get_product_by_id(filter)
#         return stripe_to_json(p)

#     if query == ProductModel.subscriptions:
#         p = get_subscriptions()
#         return stripe_to_json(p)
    
#     return JSONResponse(status_code=status.HTTP_200_OK, 
#                         content=query)




# img1 = 'https://storageapi.fleek.co/alexjslessor-team-bucket/productImg/wall6.png'
# 'https://storageapi.fleek.co/alexjslessor-team-bucket/productImg/spacescape_5.png'

# class UpdateStripe(BaseModel):
    # update: List[str]
    # update: str


# @router.post("/ecom/update_db/{query}")
# async def update_db(query: str,
                    # data: UpdateStripe):
    # print('query-ecom: ', query)
    # print('data-ecom: ', data)
    
    # product = stripe.Product.retrieve(query)
    # stripe_product_img_lst = product.images
    
    # if data.update in stripe_product_img_lst:
        # return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, 
                            # content='Image Exists')
    # else:
        # stripe_product_img_lst.append(data.update)
        # modify_product(query, images=stripe_product_img_lst)

    # return JSONResponse(status_code=status.HTTP_200_OK, 
    #                     content='Product Images Updated')
