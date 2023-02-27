# Evaluating Your Short-Position Algorithm

## Background

In this activity, you will evaluate the risk/reward characteristics of the short-position strategy that you created before.

Recall that you backtested your short-position DMAC trading algorithm in the previous activity. Now, you’ll use the backtesting data to evaluate the risk/reward characteristics of both the trading algorithm portfolio and the per-trade behaviour.

## Instructions

When you calculate the profit/loss value for each trade, remember that the difference in the case of a short-position strategy is the inverse of that for a long-position strategy. That is, you calculate the profit/loss by using the value of the entry portfolio holding minus the value of the exit portfolio holding.

Note that the starter notebook file already includes the algorithm and the backtesting steps that you completed in earlier activities. For this activity, you will run that initially provided code, then proceed to the evaluation section of the notebook file:

1. Review the provided code. This includes the `import` statements for the required libraries, the creation of the Pandas DataFrame from the `vnq.csv` file in the `Resources` folder, the code that creates and visualises the algorithm, and the code that backtests your short-position DMAC strategy.

2. Initialize a portfolio evaluation DataFrame with an index set to `['Annualized Return', 'Cumulative Returns', 'Annual Volatility', 'Sharpe Ratio', 'Sortino Ratio']` and the columns set to `['Backtest']`.

3. Calculate and assign the following portfolio evaluation metrics to the portfolio evaluation DataFrame:

    * Annualized return

    * Cumulative returns

    * Annual volatility

    * Sharpe ratio

    * Sortino ratio

4. Review the portfolio evaluation metrics, and then answer the following question: Would you advise a risk-averse investor to invest in a portfolio that uses this algorithm?

5. Initialise a trade evaluation DataFrame with the columns set to `['Stock', 'Entry Date', 'Exit Date', 'Shares', 'Entry Share Price', 'Exit Share Price', 'Entry Portfolio Holding', 'Exit Portfolio Holding', 'Profit/Loss']`.

6. Create the `for` loop to iterate through the backtested signals DataFrame, pulling the relevant entry and exit data values to calculate the per-trade profit/loss values and appending each record to the trade evaluation DataFrame.

7. Answer the following question: Based on the trade evaluation metrics, has your opinion changed regarding the advisability of this portfolio for a risk-averse investor?

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
