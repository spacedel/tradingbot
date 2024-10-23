from coinbase.rest import RESTClient

def create_client(api_key, api_secret):
    try:
        client = RESTClient(api_key=api_key, api_secret=api_secret)
        print("Client created successfully.")
        return client
    except Exception as e:
        print(f"Error creating client: {e}")
        return None
