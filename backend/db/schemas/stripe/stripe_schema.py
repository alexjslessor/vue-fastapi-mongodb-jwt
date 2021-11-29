from typing import Dict, Any, Optional, cast, List
from enum import Enum
from fastapi import (status,
                     File, 
                     UploadFile, 
                     Form, 
                     Body,
                     status, 
                     HTTPException)
from fastapi_users.password import verify_and_update_password
from fastapi.responses import JSONResponse
# from .auth_utils.override import FastAPIUsersOverride
from pydantic import  BaseModel, Field, validator, EmailStr, root_validator
from datetime import datetime, timezone
# from .config import get_settings
# from ..utils.validators import *
from bson import ObjectId
import base64
from ..fields import PyObjectId
from ..config import *
from .stripe_enum import *

# settings = get_settings()

class PydanticModels:
    
    class GetDoc(BaseModel):
        invoice_num: str
        document: str

    class UpdateCollectionDocument(BaseModel):
        event: Dict
                    
    class GetCheckout(BaseModel):
        cart_items: Dict
        
    class GetPost(BaseModel):
        post_id: str

    class GetProduct(BaseModel):
        product_id: str
        
    class UpdateStatus(BaseModel):
        event: Dict
        
    class GetQueByAddress(BaseModel):
        event: Dict
    
    class GetQueItem(BaseModel):
        event: str

    class ProductType(str, Enum):
        product = "product"
        all_active_products = "all_active_products"
        all_products = "all_products"

    class Shipping(BaseModel):
        optional: Optional[str] = None

    class LoginOauth(BaseModel):
        event: Dict



class StripeRecurring(BaseModel):
    # https://stripe.com/docs/api/prices/object#price_object-recurring-interval
     aggregate_usage: Optional[str]
     interval: Optional[StripeInterval]
     interval_count: Optional[int]
     usage_type: Optional[StripeUsageType]


class UpdateStripePriceModel(BaseModel):
    id: Optional[str]
    object: Optional[str]
    active: Optional[bool]
    billing_scheme: Optional[str]
    created: Optional[int]# unix epoch timestamp
    currency: Optional[str]
    livemode: Optional[bool]
    lookup_key: Optional[str]
    # metadata: Dict[]
    nickname: Optional[str]
    product: Optional[str]
    recurring: Optional[StripeRecurring]
    
    tiers_mode: Optional[str]
    transform_quantity: Optional[str]
    type: Optional[str]
    unit_amount: Optional[int]
    unit_amount_decimal: Optional[str]
    class Config:
        arbitrary_types_allowed = True
# {
#   "id": "price_1IfYgsLnbk9JaPUldChTTlul",
#   "object": "price",
#   "active": true,
#   "billing_scheme": "per_unit",
#   "created": 1618268230,
#   "currency": "cad",
#   "livemode": false,
#   "lookup_key": null,
#   "metadata": {},
#   "nickname": null,
#   "product": "prod_JI8yfgDh9CAncO",
#   "recurring": {
#     "aggregate_usage": null,
#     "interval": "month",
#     "interval_count": 1,
#     "usage_type": "licensed"
#   },
#   "tiers_mode": null,
#   "transform_quantity": null,
#   "type": "recurring",
#   "unit_amount": 2000,
#   "unit_amount_decimal": "2000"
# }

class UpdateStripeProductModel(BaseModel):
    id: Optional[str]
    # object: Optional[str]
    active: Optional[bool]
    created: Optional[str]
    description: Optional[str]
    
    images: Optional[List]
    image: Optional[str]
    
    livemode: Optional[bool]
    metadata: Optional[Dict]
    name: Optional[str]
    package_dimensions: Optional[str]
    shippable: Optional[str]
    statement_descriptor: Optional[str]
    unit_label: Optional[str]
    updated: Optional[str]
    url: Optional[str]
    
    class Config:
        arbitrary_types_allowed = True
        # https://pydantic-docs.helpmanual.io/usage/schema/#schema-customization
        # schema_extra = {
        #     "id": "prod_JcBrif3oQkLsTJ",
        #     "object": "product",
        #     "active": 'true',
        #     "created": '1622891745',
        #     "description": 'null',
        #     "images": '[]',
        #     "livemode": 'false',
        #     "metadata": '{}',
        #     "name": "Subscriber (1 Week Subscription) for order 73A8A6DB23",
        #     "package_dimensions": 'null',
        #     "shippable": 'null',
        #     "statement_descriptor": 'null',
        #     "unit_label": 'null',
        #     "updated": '1622891745',
        #     "url": 'null'
        # }
       

