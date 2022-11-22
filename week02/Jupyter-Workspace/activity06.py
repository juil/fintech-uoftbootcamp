"""
Conditionally Yours

Pseudocode:

"""

# Prices: float
original_price = 360.35
current_price = 293.33

# Increase: float
increase = current_price - original_price
percent_increase = increase/original_price*100

# Recommendation (string): 'buy' or 'sell'
recommendation = 'buy'

# Threshold to buy & purchase (float)
threshold_to_buy = 300
threshold_to_purchase = 300

# Balance (float)
balance = 0
portfolio_balance = 0

# Print original price
print(f'$NFLX original stock price was ${original_price:.2f}')

# Print current price
print(f'$NFLX current stock price is ${current_price:.2f}')

# Print percent increase
print(f'{percent_increase:.2f}%')

# Get recommendation based on price
if current_price <= threshold_to_buy:
    recommendation = 'buy'
else:
    recommendation = 'sell'

print(f'Recommendation: {recommendation}.')

