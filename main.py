from client import create_client
from trade_execution import execute_trade
from config import API_KEY, API_SECRET

def main():
    # Initialize client
    client = create_client(API_KEY, API_SECRET)

    # Fetch account details
    accounts = client.get_accounts()
    print("Accounts:", accounts)

    # Example of placing a trade
    execute_trade(client, "BTC-USD", "buy", amount="0.01")

if __name__ == "__main__":
    main()
