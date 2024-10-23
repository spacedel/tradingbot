import time
from trade_execution import execute_trade
from coinbase.websocket import WSClient

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def on_message(msg, rest_client):
    # Check if the message contains a price and product_id (the ticker)
    if "price" in msg and "product_id" in msg:
        product_id = msg['product_id']
        price = float(msg['price'])
        
        print(f"Received update: {product_id} at price {price}")
        
        # Example: Execute different strategies based on ticker and price
        if product_id == "BTC-USD" and price > 30000:
            execute_trade(rest_client, action="buy", product_id="BTC-USD", size="0.01")
            print("BTC-USD above 30,000, placed a buy order!")
        elif product_id == "ETH-USD" and price > 2000:
            execute_trade(rest_client, action="buy", product_id="ETH-USD", size="0.1")
            print("ETH-USD above 2,000, placed a buy order!")
        elif product_id == "ETH-USD" and price > 2000:
            execute_trade(rest_client, action="buy", product_id="ETH-USD", size="0.1")
            print("ETH-USD above 2,000, placed a buy order!")


def start_websocket(ws_client):
    # Subscribe to multiple tickers (e.g., BTC-USD and ETH-USD)
    product_ids = ["BTC-USD", "ETH-USD", "XRP-USD", "ADA-USD", "XLM-USD"]
    
    # Start the WebSocket ticker subscription for multiple products
    ws_client.ticker(product_ids=product_ids)

    # Keep the WebSocket running for a while (you can change this logic)
    time.sleep(15)  # Running the WebSocket for 15 seconds
    ws_client.close()


# Setup WebSocket Client
api_key = API_KEY
api_secret = API_SECRET
ws_client = WSClient(api_key=api_key, api_secret=api_secret, on_message=on_message)

# Subscribe to ticker channel for real-time updates on BTC-USD
ws_client.open()
ws_client.ticker(product_ids=["BTC-USD", "ETH-USD", "XRP-USD", "ADA-USD", "XLM-USD"])

# Keep connection open for 15 seconds before closing
time.sleep(15)

ws_client.ticker_unsubscribe(product_ids=["BTC-USD", "ETH-USD", "XRP-USD", "ADA-USD", "XLM-USD"])
ws_client.close()
