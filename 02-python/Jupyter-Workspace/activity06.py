"""
Conditionally Yours

Pseudocode:
    1. Set variables
        - stock, stock symbol
        - original price, current price
        - increase, percent increase
        - recommendation
        - threshold to buy, threshold to purchase
        - balance, portfolio balance
    2. Display stock, original price, current price
    3. Check if price is under threshold
    4. Recommend action (buy or sell)
    5. Check balance
        - Only recommend purchase if balance >= 5 * current price
    6. Final recommendation

"""
# Stock symbol and stock name (string)
stock = 'NFLX'
stock_name = 'Netflix'

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

'''check-balance:
    only recommend if balance >= 5 * current price'''
print(f'Current Balance: ${balance:.2f}')
affordable = balance >= 5*current_price
if recommendation == 'buy':
    if affordable:
        print('Your balance is greater than 5 times the purchase price.')
        print(f'Purchase ${stock}')
    else:
        print(f'Your balance is too low. You cannot afford to purchase ${stock} at this time.')
        print(f'Bring your balance above ${current_price*5:.2f} to purchase.')

