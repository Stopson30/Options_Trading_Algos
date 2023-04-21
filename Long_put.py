import yfinance as yf

ticker = 'AAPL'
put_option_symbol = 'AAPL220616P00150000'

# Download the put option data
option_data = yf.Ticker(put_option_symbol).info

# Check the option's price
option_price = option_data['regularMarketPrice']

# Buy the option
def buy_put(quantity):
    total_cost = quantity * option_price
    return total_cost

cost = buy_put(1)
print(f"Long Put: Total cost for 1 contract is ${cost}")
