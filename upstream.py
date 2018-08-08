import os

def get_listing_addr():
    return os.environ.get('LISTING_URI', 'http://localhost:10002/listing')


def get_product_addr():
    return os.environ.get('PRODUCT_URI', 'http://localhost:10001/product')
