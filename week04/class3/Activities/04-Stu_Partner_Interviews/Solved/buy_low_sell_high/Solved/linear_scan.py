def calculate_best_trade(prices):

    # Check if there are less than two prices in the list
    # If so, the function cannot calculate max profit
    # Else, there are at least two prices in the list and so run the function
    if len(prices) < 2:
        print("List of prices does not have at least two elements! Cannot run the function.")
    else:

        # Initialize desired number of shares
        num_shares = 10000

        # Initialize the low and high prices
        min_price = 0
        max_price = 0

        # Iterate over each price in the prices list
        for price in prices:

            # Check to see if current prices is the first entry
            # If so, set the min and max prices as the first entry
            if min_price == 0 and max_price == 0:
                min_price = price
                max_price = price
            # Check if price is less than the min price
            # If so, set the min price to the current price
            elif price < min_price:
                min_price = price
            # Check if price is greater than the max price
            # If so, set the max price to the current price
            elif price > max_price:
                max_price = price

        # Calculate the profit of the trade and round to two decimal places
        profit = round((max_price - min_price) * num_shares, 2)

        # Return both variables
        return profit

# List of stock prices for IAG between 10 AM and 11 AM (5 minute interval)
prices = [1.42, 1.32, 1.45, 1.20, 1.34, 1.74, 1.10, 1.89, 1.42, 1.90, 1.80, 1.85]

# Call the function
best_profit = calculate_best_trade(prices)

# Print the results of the function
print(f"The best profit is ${best_profit}.")
