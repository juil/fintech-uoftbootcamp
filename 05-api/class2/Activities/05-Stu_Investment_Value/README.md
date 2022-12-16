# Investment Value

As a FinTech professional, you will be using your Python and APIs coding skills to analyze financial data. In this activity, you will use the Alpaca SDK to calculate the present value of a stock portfolio.

## Instructions

Open the starter Jupyter notebook provided, and complete the following tasks.

1. Suppose you have a stock portfolio composed of `200` Microsoft (`MSFT`) shares and `320` Apple (`AAPL`) shares. Create a DataFrame named `df_shares` to store the number of shares by setting the ticker names as the index.

2. Load the environment variables from your `.env` file and save the Alpaca keys as Python variables.

3. Use your Alpaca keys to create the Alpaca API object, remember to set the `api_version` parameter to `v2`.

4. You will compute the current value in dollars of your stock portfolio. Set a variable called `today` with the current date using the ISO format.

5. You will fetch daily data, so create a variable called `timeframe` and set its value to `1Day`.

6. Use the `alpaca.get_bars()` function to retrieve the current price data for `MSFT` and `AAPL` and view the data as a DataFrame.

7. Calculate the current value in dollars of the stock using the number of shares and the current closing price you retrieved using Alpaca.

8. Add a column `values` to the original `df_shares` DataFrame and display the DataFrame.

9. Using the updated `df_shares` DataFrame, create a couple of plots to visualize your portfolio composition:

    * Create a pie chart to show the proportion of stocks in the portfolio.

    * Create a bar plot to present the current value in dollars of each ticker.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
