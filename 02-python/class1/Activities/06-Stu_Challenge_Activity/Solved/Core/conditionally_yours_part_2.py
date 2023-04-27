"""
Conditionally Yours

Pseudocode:
1. Initialize variables original_price, current_price, increase, percent_increase, recommendation, threshold_to_buy, and threshold_to_sell
2. Compute increase
3. Compute percent_increase
4. IF percent_increase is greater than or equal to threshold_to_sell
        THEN Set recommendation to "sell"
    ELSE IF percent_increase is less than or equal to threshold_to_buy
        THEN set recommendation to "buy"
    ELSE IF percent_increase is less than threshold_to_sell and greater than threshold_to_buy
        THEN set recommendation to "hold"
    ELSE
        THEN print("Not enough data to make a decision. Need human input")
5. Print("Recommendation: " + recommendation)
"""

# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create integer variable for original_price
original_price = 360.35

# Create integer variable for current_price
current_price = 293.33

# Create float for threshold_to_buy
threshold_to_buy = -10.00

# Create float for threshold_to_sell
threshold_to_sell = 20.00

# Create string for recommendation, default will be buy
recommendation = "buy"

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent increase
percent_increase = (increase / original_price) * 100

# Print original_price
print(f"Netflix's original stock price was ${original_price}")

# Print current_price
print(f"Netflix's current stock price is ${current_price}")

# Print percent increase
print(f"Netflix's stock price changed by {percent_increase:.2f}%")

# Determine if stock should be bought or sold
if percent_increase >= threshold_to_sell:
    recommendation = "sell"
elif percent_increase <= threshold_to_buy:
    recommendation = "buy"
elif percent_increase < threshold_to_sell and percent_increase > threshold_to_buy:
    recommendation = "hold"
else:
    print("Not enough data to make a decision. Need human input.")

print("Recommendation: " + recommendation)
print()
