import yfinance as yf

ticker = 'AAPL'
stock = yf.Ticker(ticker)
stock_price = stock.info['regularMarketPrice']

# Short the stock
def short_stock(quantity):
    return -quantity * stock_price

shorted_stock = short_stock(100)

# Sell the put option
def sell_put(quantity):
    total_premium = quantity * option_price
    return total_premium

premium = sell_put(1)
print(f"Covered Put: Total premium for 1 contract is ${premium}, and shorted stock value is ${shorted_stock}")
