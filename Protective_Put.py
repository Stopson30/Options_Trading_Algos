import yfinance as yf

ticker = 'AAPL'
stock = yf.Ticker(ticker)
stock_price = stock.info['lastPrice']

# Buy the stock
def buy_stock(quantity):
    return quantity * stock_price

owned_stock = buy_stock(100)

# Buy the put option
cost = buy_put(1)

print(f"Protective Put: Total cost for 1 put contract is ${cost}, and owned stock value is ${owned_stock}")
