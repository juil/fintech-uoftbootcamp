# Calculating Correlation Using Pandas DataFrames

In this exercise, you will learn how to calculate correlation between the respective closing stock prices and daily stock returns of MSFT and SP500.

## Instructions

1. Import the `pandas`, `pathlib`, and `seaborn` libraries, and set the `%matplotlib inline` property.

2. Create a two variables `msft_csv_path` and `sp500_csv_path` that represents the path to the [MSFT.csv](Resources/MSFT.csv) and [SP500.csv](Resources/SP500.csv) using the Pathlib library.

3. Read the CSVs into Pandas DataFrames.

4. Combine the DataFrames by concatenating by columns and performing an inner join.

5. Drop the extra columns (everything except closing prices).

6. Rename the columns to reflect the respective stock closing prices (MSFT or SP500).

7. Use a line chart to plot the closing price trends for MSFT and SP500.

8. Use a scatter plot to plot the price relationships between MSFT and SP500.

9. Calculate the correlation of closing stock prices between MSFT and SP500.

10. Use the `seaborn` heatmap to plot the correlation of closing stock prices between MSFT and SP500.

11. Calculate the daily returns for the combined DataFrame.

12. Use a line chart to plot the daily return trends for MSFT and SP500.

13. Use a scatter plot to plot the daily return relationships between MSFT and SP500.

14. Calculate the correlation of daily returns for MSFT and SP500.

15. Use the `seaborn` heatmap to plot the correlation of daily stock returns between MSFT and SP500.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
