import time
from coinbase.rest import RESTClient
from json import dumps
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)

# Define the product IDs for multiple cryptocurrencies
PRODUCT_IDS = ["BTC-USD", "XRP-USD", "ADA-USD", "ETH-USD", "XLM-USD"]

def get_balance():
    accounts = client.get_accounts()
    return {acc['currency']: acc['balance']['amount'] for acc in accounts['data']}

def get_current_prices(product_ids=PRODUCT_IDS):
    prices = {}
    for product_id in product_ids:
        print(f"Fetching price for {product_id}...")  # Log the product being fetched
        try:
            # Fetch the ticker data for the specified product_id
            price_data = client.get_product_book(product_id=product_id)

            # Log the raw data received for debugging
            print(f"Raw data for {product_id}: {price_data}")  

            # Ensure price_data is not None and has a 'price' key
            if price_data and 'price' in price_data:
                prices[product_id] = float(price_data['price'])
                print(f"Price for {product_id}: {prices[product_id]}")
            else:
                prices[product_id] = None
                print(f"Warning: Price data for {product_id} is invalid or not found.")
                
        except Exception as e:
            print(f"Error fetching price for {product_id}: {e}")
            prices[product_id] = None  # Set price to None if there's an error

    return prices

def execute_buy_order(product_id, size="0.001"):
    order = client.market_order_buy(client_order_id="", product_id=product_id, quote_size=size)
    print(dumps(order, indent=2))

def execute_sell_order(product_id, size="0.001"):
    order = client.market_order_sell(client_order_id="", product_id=product_id, base_size=size)
    print(dumps(order, indent=2))

def trading_bot():
    while True:
        print("Checking current prices...")  # Log before checking prices
        prices = get_current_prices()
        print("Current Prices:", prices)
        
        # Add your trading logic here based on the prices dictionary
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    trading_bot()
