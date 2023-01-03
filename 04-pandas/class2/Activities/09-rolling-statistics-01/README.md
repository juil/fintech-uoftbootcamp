# Visualizing Rolling Statistics with Pandas DataFrames

In this exercise you will learn how to calculate and visualize rolling statistics pertaining to a specified time window.

## Instructions

1. Import the `pandas` and `pathlib` libraries, and set the `%matplotlib inline` property.

2. Create a variable `csvpath` that represents the path to the [MSFT.csv](Resources/MSFT.csv) using the Pathlib library.

3. Read the CSV into a Pandas DataFrame.

4. Drop the extra columns: 'volume', 'open', 'high', 'low'.

5. Plot the daily closing prices of MSFT.

6. Use the `rolling`, `mean`, and `plot` functions to calculate a 7 day rolling window of average MSFT closing prices.

7. Use the `rolling`, `mean`, and `plot` functions to calculate a 7 day rolling window of standard deviation for MSFT closing prices.

8. Use the `rolling`, `mean`, and `plot` functions to calculate a 30 day rolling window of average MSFT closing Prices

9. Use the `rolling`, `mean`, and `plot` functions to calculate a 30 day rolling window of standard deviation for MSFT closing prices.

10. Use the `rolling`, `mean`, and `plot` functions to calculate a 180 day rolling window of average MSFT closing prices.

11. Use the `rolling`, `mean,` and `plot` functions to calculate a 180 day rolling window of standard deviation for MSFT closing prices.

12. Overlay the plot for a 180 day rolling mean of MSFT on top of the daily closing prices of MSFT. Use the `plot` function with the `ax` parameter to overlay multiple plots.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
