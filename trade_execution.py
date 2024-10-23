def execute_trade(client, product_id, side, amount=None):
    try:
        if side == "buy":
            order = client.market_order_buy(product_id=product_id, base_size=amount)
        elif side == "sell":
            order = client.market_order_sell(product_id=product_id, base_size=amount)
        else:
            raise ValueError("Invalid side. Choose 'buy' or 'sell'.")

        print(f"Trade executed: {order}")
    except Exception as e:
        print(f"Error executing trade: {e}")
