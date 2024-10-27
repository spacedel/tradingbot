# trading_library.py

from coinbase.wallet.client import Client

def initialize_client(api_key, api_secret):
    return Client(api_key, api_secret)

def get_balance(client):
    accounts = client.get_accounts()
    return {account['currency']: account['balance']['amount'] for account in accounts['data']}

def get_price(client, ticker):
    # Assume you have a function that fetches price from an exchange
    return client.get_spot_price(currency_pair=ticker)['amount']
