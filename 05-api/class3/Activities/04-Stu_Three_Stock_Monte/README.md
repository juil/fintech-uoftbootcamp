# Three Stock Monte

Recently you received an annual bonus from your company of $15,000 for all of your hard work over the past year. Since you have no immediate vacations planned or bills to pay, you decide the best use of this new money is to invest it across a few stocks and let it grow. In order to decrease risk and maximize return, you want to invest your bonus into three stocks - AT&T (`T`), Nike (`NKE`), and Exxon Mobil (`XOM`). However, you are unsure how much of each stock to buy.

Your job is to use your API knowledge and the `MCForecastTools.py` toolkit to determine how much of each stock to purchase in order to maximize your chances of profit.

## Instructions

Using the starter code complete the following steps.

1. Copy the starter code and the `MCForecastTools` in the same working directory.

2. Import the necessary libraries and dependencies.

3. Create a `.env` file in the same directory as your starter code.

4. Inside the `.env` file, include a variable for `ALPACA_API_KEY` and `ALPACA_SECRET_KEY` to access the Alpaca API.

5. Setup the Alpaca API environment

6. Using the Alpaca API, query the database and get approximately four year's worth of daily stock information (4*252 trading days) for the following stocks:

    * `T` - AT&T
    * `NKE` - Nike
    * `XOM` - Exxon Mobil

7. Create an instance of `MCSimulation` that simulates the next five years of portfolio returns with the following parameters:

    * Set the `weights` parameter to `[.33,.33,.33]` to invest evenly across all `3` stocks.

    * Set the `num_simulation` parameter to `1000` to ensure that your simulation is reliable.

    * Set the `num_trading_days` parameter to `252*5` to simulate `5` years of trading days.

8. Run the Monte Carlo simulation and visualize the results of the simulation using `MCSimulation` built-in methods (`plot_simulation()`, `plot_distribution()` and `summarize_cumulative_return()`).

9. Using the `95%` confidence interval and your initial investment of $15,000, determine the lower limit and upper limit of your expected portfolio value after `5` years of growth.

10. Create a second instance of `MCSimulation` with the same attributes, except set the `weights` variable to `[.20,.60,.20]` to represent a portfolio with a majority of AT&T stock.

11. Run the Monte Carlo simulation using your new weights. Once complete, use the 95% confidence interval and your initial investment of $15,000, determine what the lower limit and upper limit of your expected portfolio value after `5` years of growth is.

12. Create a third instance of `MCSimulation` using the same attributes, except set the `weights` variable to `[.60,.20,.20]` to represent a portfolio with a majority of Nike stock.

13. Once again, run the Monte Carlo simulation using your new weights. Once complete, use the 95% confidence interval and your initial investment of $15,000, determine what the lower limit and upper limit of your expected portfolio value after `5` years of growth is.

14. Create a fourth instance of `MCSimulation` using the same attributes, except set the `weights` variable to `[.20,.20,.60]` to represent a portfolio with a majority of Exxon stock.

15. Once more, run the Monte Carlo simulation using your new weights. When complete, use the 95% confidence interval and your initial investment of $15,000, determine what the lower limit and upper limit of your expected portfolio value after `5` years of growth is.

16. Lastly, look across all four simulated portfolios and determine which set of investments gives you the best chances of profit. In your notebooks, write which portfolio you chose and why.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
