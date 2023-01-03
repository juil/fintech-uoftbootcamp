def calculate_best_trade(prices):

    # Check whether there are less than two prices in the list
    # If so, the function cannot calculate maximum profit
    # Else, there are at least two prices in the list and so run the function
    if len(prices) < 2:
        print("List of prices does not have at least two elements! Cannot run the function.")
    else:
        # Initialize desired number of shares
        num_shares = 10000
    
        # Initialize max profit variable
        max_profit = 0
    
        # Loop over every price in the prices list
        for price_one in prices:
            # Print price_one
            print(price_one)
    
            # Loop over every price in the prices list again
            for price_two in prices:
    
                # Calculate the profit for every pair/combination of the prices list
                profit = round(price_two - price_one, 2)
    
                # If max_profit is equal to 0, set max_profit to the first profit calculated
                # Else if the current profit is greater than the max_profit, set max_profit to the current profit
                if max_profit == 0:
                    max_profit = profit
                elif profit > max_profit:
                    max_profit = profit
    
                # Print price_two, profit, and max_profit
                print(f"  {price_two} : {profit} : {max_profit}")
    
        # Calculate total profit in terms of money
        total_profit = max_profit * num_shares
    
        # Return total_profit variable
        return(total_profit)

# List of stock prices for IAG between 10 AM and 11 AM (5 minute interval)
prices = [1.42, 1.32, 1.45, 1.20, 1.34, 1.74, 1.10, 1.89, 1.42, 1.90, 1.80, 1.85]

# Call the function
best_profit = calculate_best_trade(prices)

# Print the results of the function
print(f"The best profit is ${best_profit}.")
