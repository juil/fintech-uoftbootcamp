# Hello Variable World Activity

# Formulas Needed:
# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create float variable for original_price
original_price = 100.0

# Create float variable for current_price
current_price = 120.0

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent_increase
percent_increase = increase/original_price*100

# Print original_price
print(f"Apple's original stock price was ${original_price:.2f}")

# Print current_price
print(f"Apples current stock price is ${current_price:.2f}")

# Print percent_increase
print(f"Apple's stock price increased by {percent_increase:.2f}%")

# CHALLENGE:
# Use a format specifier with the f-string to print the percent increase with two decimal places: