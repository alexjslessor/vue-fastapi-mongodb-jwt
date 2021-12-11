import stripe
from pprint import pprint
from json import loads, dumps
# from ...config.config import get_settings
from ...settings import get_settings

settings = get_settings()

stripe.api_key = settings.STRIPE_SECRET_ALEXJSLESSOR
assert len(stripe.api_key) > 0

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

    return c['id']

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
    