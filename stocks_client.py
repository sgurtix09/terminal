import requests

class StocksClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://finnhub.io/api/v1"

    def fetch_stock_price(self, symbol):
        url = f"{self.base_url}/quote?symbol={symbol}&token={self.api_key}"
        response = requests.get(url)
        return response.json()  # Returns current price info

    def fetch_stock_data(self, symbols):
        data = {}
        for symbol in symbols:
            data[symbol] = self.fetch_stock_price(symbol)
        return data

# Usage Example:
if __name__ == '__main__':
    api_key = 'YOUR_FINNHUB_API_KEY'
    client = StocksClient(api_key)
    popular_stocks = ['MSTR', 'SOFI', 'CRCL', 'AAPL', 'MSFT', 'NVDA', 'TSLA']
    stocks_data = client.fetch_stock_data(popular_stocks)
    print(stocks_data)
