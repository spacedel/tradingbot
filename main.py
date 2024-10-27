# main.py

from trade_execution import trading_bot

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


if __name__ == "__main__":
    trading_bot(API_KEY, API_SECRET)
