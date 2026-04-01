import requests

class HyperliquidClient:
    BASE_URL = 'https://api.hyperliquid.com/api/v1/'

    def __init__(self):
        pass

    def fetch_data(self, endpoint, params=None):
        url = f'{self.BASE_URL}{endpoint}'
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    def get_markets(self):
        return self.fetch_data('markets')

    def get_market_data(self, market_id):
        return self.fetch_data(f'markets/{market_id}')

    def get_trade_history(self, market_id, params=None):
        return self.fetch_data(f'markets/{market_id}/trades', params=params)

# Example usage:
# client = HyperliquidClient()
# markets = client.get_markets()
# print(markets)