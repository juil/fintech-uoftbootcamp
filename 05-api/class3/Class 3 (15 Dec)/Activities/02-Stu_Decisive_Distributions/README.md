# Decisive Distributions

You have been working as a financial analyst for Investments4You for over a year. Today, your boss stopped by your desk and asked for your help.

She explained that she is trying to put together a presentation and wants something that can help visualize the differences in volatility across several potential stocks.

Your job is to build visualizations that compare stock volatility in terms of daily returns.

## Instructions

Using the starter code complete the following steps.

1. Import the necessary libraries and dependencies.

2. Create a `.env` file in the same directory as your starter code.

3. Inside the `.env` file, include a variable for `ALPACA_API_KEY` and `ALPACA_SECRET_KEY` to access the Alpaca API.

4. Setup the Alpaca API environment

5. Using the Alpaca API, query the database and get 1 year's worth of daily stock information for the following stocks:

    * `SPY` - SPDR S&P 500 ETF Trust

    * `LUV` - Southwest Airlines

    * `DIS` - Disney

    * `AAPL` - Apple

    * `SBUX` - Starbucks

    * `WORK` - Slack

    > **Hint:** Use the same workflow from the past lesson to run your query using the Alpaca SDK. Be sure to set your `timeframe`, `start` and `end` dates, and your `ticker` information!

6. Create a new DataFrame and store the closing prices of each stock.

7. Calculate the daily returns for each stock using the `pct_change()` function

8. Visualize the distribution of daily returns across all stocks using a histogram plot.

    > **Hint:** You can make the visualization more readable by changing aesthetics such as the `alpha` argument to `0.5`.

9. Visualize the distribution of daily returns across all stocks using a density plot.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
