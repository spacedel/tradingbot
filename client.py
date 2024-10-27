import os
import time
from dotenv import load_dotenv
from coinbase.rest import RESTClient
from coinbase.websocket import WSClient

# Load environment variables from .env file
load_dotenv()

# Fetch API credentials from environment variables
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Function to handle messages received from the WebSocket
def on_message(msg):
    print("Received WebSocket Message:", msg)

# Function to open and subscribe to WebSocket channels
def start_websocket():
    ws_client = WSClient(api_key=API_KEY, api_secret=API_SECRET, on_message=on_message)
    
    # Open WebSocket connection
    ws_client.open()
    
    # Subscribe to ticker and heartbeat channels for BTC-USD and ETH-USD
    ws_client.subscribe(product_ids=["BTC-USD", "ETH-USD", "XRP-USD", "ADA-USD", "XLM-USD"], channels=["ticker", "heartbeats"])

    # Keep the connection open for 10 seconds to receive messages
    time.sleep(10)

    # Unsubscribe and close the connection
    ws_client.unsubscribe(product_ids=["BTC-USD", "ETH-USD", "XRP-USD", "ADA-USD", "XLM-USD"], channels=["ticker", "heartbeats"])
    ws_client.close()

# Function to fetch current prices via REST API
def fetch_current_prices():
    rest_client = RESTClient(api_key=API_KEY, api_secret=API_SECRET)
    
    # Fetch the ticker data for BTC-USD and ETH-USD
    btc_ticker = rest_client.get_product_book(product_id="BTC-USD")
    eth_ticker = rest_client.get_product_book(product_id="ETH-USD")
    xrp_ticker = rest_client.get_product_book(product_id="XRP-USD")
    ada_ticker = rest_client.get_product_book(product_id="ADA-USD")
    xlm_ticker = rest_client.get_product_book(product_id="XLM-USD")
    
    print("Current BTC Ticker (REST):", btc_ticker)
    print("Current ETH Ticker (REST):", eth_ticker)
    print("Current ETH Ticker (REST):", xrp_ticker)
    print("Current ETH Ticker (REST):", ada_ticker)
    print("Current ETH Ticker (REST):", xlm_ticker)


if __name__ == "__main__":
    # Fetch current prices using REST
    fetch_current_prices()
    
    # Start WebSocket for real-time updates
    start_websocket()


