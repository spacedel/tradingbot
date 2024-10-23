import time
import logging
import numpy as np
import pandas as pd
from client import rest_client
from trading_library import execute_trade, get_price, get_balance, get_historical_data

# Set up logging
logging.basicConfig(level=logging.INFO, filename='trading_log.txt', 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Define trading parameters
tickers = {
    "BTC-USD": {"size": 0.01, "profit_target": 35000, "stop_loss": 29000},
    "ETH-USD": {"size": 0.1, "profit_target": 2500, "stop_loss": 1800},
}

# Risk management function to calculate position size
def calculate_position_size(account_balance, risk_per_trade=0.01):
    return account_balance * risk_per_trade

# Function to check for technical indicators (e.g., simple moving average)
def calculate_sma(data, period=5):
    return data['close'].rolling(window=period).mean().iloc[-1]

# Function to check conditions and execute trades
def check_and_trade(ticker, size, profit_target, stop_loss):
    current_price = get_price(ticker)
    historical_data = get_historical_data(ticker)  # Get historical data for indicators

    if len(historical_data) > 0:
        historical_data['sma'] = calculate_sma(historical_data)
        current_sma = historical_data['sma'].iloc[-1]

        # Check for buy conditions based on SMA
        if current_price > current_sma:
            execute_trade(rest_client, action="buy", product_id=ticker, size=size)
            logging.info(f"{ticker} bought at {current_price} (SMA: {current_sma})")

        # Check for profit target and stop-loss conditions
        if current_price >= profit_target:
            execute_trade(rest_client, action="sell", product_id=ticker, size=size)
            logging.info(f"{ticker} sold at {current_price} for profit target reached!")
        elif current_price <= stop_loss:
            execute_trade(rest_client, action="sell", product_id=ticker, size=size)
            logging.info(f"{ticker} sold at {current_price} for stop-loss triggered!")

# Main trading loop
def trading_bot():
    while True:
        account_balance = get_balance()
        position_size = calculate_position_size(account_balance)

        for ticker, params in tickers.items():
            check_and_trade(ticker, position_size * params["size"], params["profit_target"], params["stop_loss"])
        
        time.sleep(60)  # Delay between checks

# Start the bot
if __name__ == "__main__":
    logging.info("Starting trading bot...")
    trading_bot()
