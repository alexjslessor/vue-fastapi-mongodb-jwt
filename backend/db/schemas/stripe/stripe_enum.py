from enum import Enum

class StripeInterval(str, Enum):
    month = 'month'
    year = 'year'
    week = 'week'
    day = 'day'
    
class StripeUsageType(str, Enum):
    metered = 'metered'
    licensed = 'licensed'

class ProductModel(str, Enum):
    all_products = "all_products"
    single_product = 'product_id'
    subscriptions = 'subscriptions'
    all_mongo_products = 'all_mongo_products'