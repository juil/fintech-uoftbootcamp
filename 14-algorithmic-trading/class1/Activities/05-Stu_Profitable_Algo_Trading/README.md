# Profitable Algorithmic Trading

In this activity, you’ll write a trading algorithm that buys 100 shares of AMD stock on the days when the price decreases and that sells the accumulated shares on the last day of the trading period.

## Background

After a successful presentation of your trading algorithm to the Board of Directors, they asked you to meet with the Trading Strategies Team to modify your current algorithm to include metrics that can aid customers in evaluating the profitability of the algorithmic trading strategy.

After meeting with the Trading Strategies Team, you were asked to include costs, proceeds, and return on investments metrics to assess the profitability of your trading algorithm.

## Instructions

1. Open the starter code provided. Run the cells of the "Data Loading" section to create the DataFrame with the AMD stock closing data.

2. Using the starter code provided, change the algorithm by modifying the loop to include the cost and proceeds metrics for buys of 100 shares. Make sure that the algorithm checks the following conditions and executes the strategy for each one:

    * If `previous_price == 0`, use the `loc` function to set the “trade_type” column for the current index to “buy”. Set the “cost/proceeds” column to the current share price multiplied by a `share_size` value of 100. Make sure to take the negative value of the expression so that the cost reflects money leaving an account. Finally, make sure to add the bought shares to an `accumulated_shares` variable.

    * Otherwise, if the price of the current day is less than that of the previous day, set the “trade_type” column of the current index to “buy”. Set the “cost/proceeds” column to the current share price multiplied by a `share_size` value of 100. Make sure to take the negative value of the expression so that the cost reflects money leaving an account. Finally, make sure to add the bought shares to an `accumulated_shares` variable.

    * You will not modify the algorithm for instances where the current day’s price is greater than the previous day’s price or when it is equal to the previous day’s price.

    * If the current index is equal to the last index of the DataFrame, set the “trade_type” column for the current index to “sell”. (Use the `index` function to check the current index.) In this case, also set the “cost/proceeds” column to the total number in the `accumulated_shares` variable multiplied by the price of the last day.

3. Run the updated algorithm. Then review the “cost/proceeds” column in the resulting DataFrame to confirm two results. First, the dates that have a “trade_type” of “buy” should have cost values in this column. Second, the final date should have a proceeds value in this column.

4. Calculate the total profit or loss for the trading algorithm by summing the values in the "cost/proceeds" column. Print the value of the total profit or loss from the trades.

    > **Hint** Use the `sum` and `round` functions to sum the values in the “cost/proceeds” column.

5. Calculate the ROI for the trades. To do so, first calculate the invested capital (the total cost of all the buys). Then divide the total profit or loss by the cost of all the buys to determine the ROI. Finally, print the value of the ROI.

## References:

* [Pandas `sum` function documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html)

* [Pandas `round` function documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html)

* [Pandas `iterrows` function documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html)

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
