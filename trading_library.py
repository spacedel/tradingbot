import time
from coinbase.rest import RESTClient

# Initialize the REST client
def create_client(api_key, api_secret):
    return RESTClient(api_key=api_key, api_secret=api_secret)

def execute_trade(client, action, product_id, size):
    if action == "buy":
        order = client.market_order_buy(client_order_id=None, product_id=product_id, size=size)
        print(f"Buy order placed for {size} of {product_id}: {order}")
    elif action == "sell":
        order = client.market_order_sell(client_order_id=None, product_id=product_id, size=size)
        print(f"Sell order placed for {size} of {product_id}: {order}")

def get_price(client, product_id):
    product = client.get_product(product_id)
    return float(product.price)

def get_balance(client):
    accounts = client.get_accounts()
    balance = {account.currency: account.available_balance['value'] for account in accounts.accounts}
    return balance

def get_historical_data(client, product_id, start_time, end_time):
    return client.get_product_historic_rates(product_id, start=start_time, end=end_time)
