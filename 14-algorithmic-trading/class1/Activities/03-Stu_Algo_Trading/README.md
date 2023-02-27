# Getting Started with Algorithmic Trading

In this activity, you’ll write a trading algorithm that uses Python to represent the conditions of a simple trading strategy.

## Background

You work on a trading firm that started operations a century ago. The firm is well consolidated and has prominent customers. As a FinTech professional, you were hired to drive innovation. Your manager asked you to prepare a prototype to show algorithmic trading capabilities to the Board of Directors so they can understand how it works.

You decided to start with a simple trading algorithm based on rules and Python conditionals to present the fundamentals of transforming a mental trading strategy into functional Python code.

## Instructions

1. Using the data that the starter notebook supplies, run the code cells that import the required libraries, and then create a Pandas DataFrame named `amd_df`.

2. Use the Pandas `bdate_range` function to assign dates to the values in the DataFrame. Set the dates as the DataFrame index. Use `2019-09-30` for the starting date.

3. Visualize the price movement of the DataFrame by using the Pandas `plot` function.

4. Add a column named “trade_type” to the DataFrame that will hold the buys and sells and set it equal to `np.nan`. Then, initialise a variable named `previous_price` that is set equal to `0`.

5. Write an algorithm that loops through each index and row of the DataFrame by using the Pandas `iterrows` function. Make sure that the algorithm checks the following conditions and executes the strategy for each one:

    * If `previous_price == 0`, use the `loc` function to set the “trade_type” column for the current index to “buy”.

    * Otherwise, if the price of the current day is less than that of the previous day, set the “trade_type” column for the current index to “buy”.

    * Otherwise, if the price of the current day is greater than that of the previous day, set the “trade_type” column for the current index to “sell”.

    * Otherwise, if the price of the current day is equal to that of the previous day, set the “trade_type” column of the current index to “hold”.

    * If the current index is equal to the last index of the DataFrame, set the “trade_type” column for the current index to “sell”. (Use the `index` function to check the current index.)

6. Run the algorithm. Then review the resulting DataFrame to confirm that given the closing prices, the “trade_type” column populated as expected.

## References

* [Pandas `bdate_range` function documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.bdate_range.html)

* [Pandas `iterrows` function documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html)

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
