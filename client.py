from flask import Flask
from flask import render_template
import requests
import upstream
import socket

app = Flask(__name__)

def get_products():
    try:
        products = requests.get(upstream.get_product_addr())
        print(products.status_code)
        print(products.text)
        return products.json()
    except requests.ConnectionError as e:
        return []

def get_listings():
    try:
        listings = requests.get(upstream.get_listing_addr())
        print(listings.status_code)
        print(listings.text)
        return listings.json()
    except requests.ConnectionError as e:
        return []

@app.route('/healthz')
def healthz():
    return 'OK'

@app.route('/')
def index():
    products = get_products()
    listings = get_listings()
    return render_template('index.html', prod_list=products, listings_list=listings, hostname=socket.gethostname())

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
