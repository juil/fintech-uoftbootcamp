# Profitable Algorithmic Trading

In this activity, you’ll backtest an algorithm to determine both the changes to the overall portfolio values and the daily return and cumulative return metrics. In doing so, you'll focus on trading "short" strategies, meaning strategies designed to profit from price falls.

## Background

Remember the short-position DMAC trading algorithm that you developed in the previous lesson? You’ll revisit that algorithm and backtest the short-position strategy that it used to trade VNQ stock during the 2008 recession.

## Instructions

1. Review the provided code. This includes the `import` statements for the required libraries, the creation of the Pandas DataFrame from the `vnq.csv` file in the `Resources` folder, and the code that creates and visualises the short-position DMAC trading algorithm.

2. Set an `initial_capital` variable to `100000` to represent the starting value ($100,000) of your simulated portfolio. Be sure to create this variable as a floating point number.

3. Set a `share_size` variable to negative 500 shares (-500).
    > **Note:** Remember that you’re using a short-position strategy. The objective is to enter the trade by selling shares at a high price before buying them back, or exiting the trade, at a lower price.

4. Create a new column named “Position” by multiplying the `share_size` value by the values in the “Signal” column.

5. Create a new column named “Entry/Exit Position” by calling the `diff` function on the “Position” column.

6. Create a new column named “Portfolio Holdings” by multiplying the “Close” prices of VNQ by the values in the “Position” column.

7. Create a new column named “Portfolio Cash” by subtracting the cumulative sum of the trades that the “Entry/Exit Position” column indicates from the `initial_capital` value.

8. Create a new column named “Portfolio Total” by adding the values of the “Portfolio Cash” and “Portfolio Holdings” columns.

9. Create a new column named “Portfolio Daily Returns” by calling the `pct_change` function on the “Portfolio Total” column.

10. Create a new column named “Portfolio Cumulative Returns” by calling the `cum_prod` function on the “Portfolio Daily Returns” column.

11. Use the `hvplot` function to plot the short-position DMAC trading strategy against its backtesting results.

12. Review the resulting overlay plot. Then answer the following question: Does it appear that this algorithm suits a short-position trading strategy?

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
