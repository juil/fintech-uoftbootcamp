# Calculating Portfolio Returns with Pandas DataFrames

In this activity, you will learn how to calculate portfolio returns with a 60-40 capital allocation for MSFT and the S&P 500, respectively.

## Instructions

1. Import the `pandas` and `pathlib` libraries, and set the `%matplotlib inline` property.

2. Create two variables named `msft_csv_path` and `sp500_csv_path` that represent the paths to [MSFT.csv](Resources/MSFT.csv) and [SP500.csv](Resources/SP500.csv) using the Pathlib library.

3. Import the CSVs into Pandas DataFrames.

4. Use the `concat` function to combine the two DataFrames by columns and an inner join, and then sort the index in ascending order.

5. Drop the extraneous columns: 'volume', 'open', 'high', 'low'.

6. Rename the columns to the respective stock (MSFT or S&P 500)

7. Use the `pct_change` function to calculate the daily returns of each stock.

8. Use the `dot` function to multiply a list of weights by the daily return of each corresponding stock.

9. Plot the daily portfolio returns.

10. Use the `cumprod` function to cumulatively multiply the daily portfolio returns to calculate the cumulative portfolio returns.

11. Plot the cumulative portfolio returns.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
