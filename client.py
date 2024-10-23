from coinbase.rest import RESTClient
from coinbase.websocket import WSClient

def rest_client(api_key, api_secret):
    return RESTClient(api_key=api_key, api_secret=api_secret)

def ws_client(api_key, api_secret, on_message):
    return WSClient(api_key=api_key, api_secret=api_secret, on_message=on_message)

