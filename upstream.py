import os

# At some point this could be dynamic.
# But for now, use the local proxy
def get_listing_addr():
    listing_addr = os.environ.get('')
    return "{0}/listing".format(os.getenv('LISTING_URI','http://localhost:10002/listing'))


def get_product_addr():
    return "{0}/product".format(os.getenv('PRODUCT_URI', 'http://localhost:10001/product'))