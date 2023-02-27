# Evaluating Algorithmic Strategy Performance

In this activity, you will be utilising the performance metrics you've learned in order to analyse the benefits and tradeoffs of various algorithmic strategy investments.

## Instructions

#### Read in the Data

* Using the Jupyter notebook included in the unsolved folder, import the [data on daily returns to various algorithmic strategies.](Resources)

* This starter code reads in the following datasets:
  * `option_algos.csv`: Daily returns to an algorithmic option strategy on three stocks.
  * `option_trades.csv`: The number of trades each day for the three option strategies.
  * `equity_algos.csv`: Daily returns to an algorithmic equity strategy on three stocks.
  * `equity_trades.csv`: The number of trades each day for the three equity strategies.

#### Plotting Performance

* Plot non-compounded returns (`cumsum`) to the three option strategies.

* Plot compounded returns (1+`cumprod`) to the three equity strategies.

#### Adding Transaction Costs

* Create a variable called `cost_per_trade`, setting it at 0.001 (0.10% per trade).

* Using the `equity_trades` DataFrame, calculate the daily trade costs for each equity in the `equity_trades` DataFrame.

* Create a new DataFrame called `equity_returns_after_cost`, which subtracts daily trade costs from the `equity_returns` DataFrame.

* Then, create a new variable called `cost_per_trade`, this time setting it at 0.005 (0.50% per trade). Similarly, create a `option_returns_after_cost` DataFrame, which takes the daily option returns, and subtracts out daily `cost_per_trade` for the options.

#### Plot Performance After Transaction Costs

* Using 1+`cumprod`, calculate and plot cumulative performance of the `equity_returns_after_cost`.

* Using `cumsum`, calculate the total performance of the option returns `option_returns_after_cost`.

#### Calculate Sharpe Ratios

* Using the returns **after transaction costs**, calculate the Sharpe Ratio for each strategy
  * Calculate the Sharpe Ratios for both equity and option strategies.

#### Calculate Weekly Returns

* Use groupby on the equity returns (after transaction costs) and calculate total (`sum`) weekly returns. Use `describe` to display the best and worst weeks for trading.

* Do the same groupby approach, this time looking at weekly option trading returns.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
