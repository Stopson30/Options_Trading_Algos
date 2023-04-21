import yfinance as yf

ticker = 'AAPL'
put_option_symbol1 = 'AAPL220616P00150000'
put_option_symbol2 = 'AAPL220616P00140000'

# Download the put option data
option_data1 = yf.Ticker(put_option_symbol1).info
option_data2 = yf.Ticker(put_option_symbol2).info

# Check the option's prices
option_price1 = option_data1['regularMarketPrice']
option_price2 = option_data2['regularMarketPrice']

# Buy the first put option and sell the second put option
def vertical_put_spread(quantity):
    total_cost = (option_price1 - option_price2) * quantity
    return total_cost

cost = vertical_put_spread(1)
print(f"Vertical Put Spread: Total cost for 1 contract is ${cost}")
