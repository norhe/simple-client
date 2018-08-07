#!/usr/bin/env python
import os
# At some point this could be dynamic.
# But for now, use the local proxy
def get_listing_addr():
    return "{0}/listing".format(os.environ.get("LISTING_ADDR", 'http://localhost:10002'))


def get_product_addr():
    return "{0}/product".format(os.environ.get("PRODUCT_ADDR", "http://localhost:10001"))