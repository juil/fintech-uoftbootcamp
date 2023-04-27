# Hello Variable World Activity

# Formulas Needed:
# Increase = Current Price - Original Price
# Percent Increase = Increase / Original x 100

# Create float variable for original_price
original_price = 198.87

# Create float variable for current_price
current_price = 254.32

# Calculate difference between current_price and original_price
increase = current_price - original_price

# Calculate percent increase
percent_increase = (increase / original_price) * 100

# Print original_price
print(f"Apple's original stock price was ${original_price}")

# Print current_price
print(f"Apple's current stock price is ${current_price}")

# Print percent increase
print(f"Apple's stock price increased by ${percent_increase}")

# CHALLENGE:
# Use a format specifier with the f-string to print the percent increase with two decimal places:
print(f"Apples percent increase in price is {percent_increase:.2f}%")