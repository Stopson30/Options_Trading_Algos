import yfinance as yf

ticker = 'AAPL'
put_option_symbol = 'AAPL220616P00150000'

# Download the put option data
option_data = yf.Ticker(put_option_symbol).info

# Check the option's price
option_price = option_data['lastPrice']

# Buy the option
def buy_put(quantity):
    total_cost = quantity * option_price
    return total_cost

cost = buy_put(1)

# Buy the stock
def buy_stock(quantity):
    stock = yf.Ticker(ticker)
    stock_price = stock.info['regularMarketPrice']
    return quantity * stock_price

owned_stock = buy_stock(100)

print(f"Protective Put: Total cost for 1 put contract is ${cost:.2f}, and owned stock value is ${owned_stock:.2f}")
