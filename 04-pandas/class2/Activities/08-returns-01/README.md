# Calculating Stock Returns via Pandas DataFrame

In this exercise you will learn how to calculate daily stock returns and cumulative stock returns.

## Instructions

Perform the following:

1. Import the `pandas` and `pathlib` libraries, and set the `%matplotlib inline` property.

2. Create a variable `csvpath` that represents the path to the [MSFT.csv](Resources/MSFT.csv) using the Pathlib library.

3. Read the CSV into a Pandas DataFrame.

4. Drop the extra columns: 'volume', 'open', 'high', 'low'.

5. Format and set the `date` column as the index to the DataFrame; use the `to_datetime` function with the `infer_datetime_format` parameter set to `True` to format the `date` column and then use the `set_index` function to set the formatted `date` column as the index to the DataFrame.

6. Drop the extra `date` column, as the index now contains the `date` column values.

7. Plot the daily close values of MSFT.

8. Use the `pct_change` function to calculate the daily returns of MSFT.

9. Plot the daily return values for MSFT.

10. Use the `cumprod` function to calculate the cumulative returns of MSFT.

11. Plot cumulative return values for MSFT.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
