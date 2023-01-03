# Returns Over Date Ranges

Harold's manager wants him to analyze the last 4 years of historical price data for Shopify, and then plot the daily returns over the previous 1-, 2-, 3-, and 4-year periods. His manager wants to see the differences in average daily returns for each time period to determine whether a short- or long-term perspective should be used in prospecting Shopify as a potential investment opportunity.

Use the following instructions to help Harold analyze the last 4 years of Shopify stock data.

## Instructions

Use the starter file to complete the following steps.

  1. Import the necessary libraries and dependencies.

  1. Read in `shopify_stock_data.csv` as a Pandas DataFrame.

  1. Display summary statistics of the input data to get a feel for your data.

  1. Drop the `volume`, `open`, `high`, and `low` columns.

  1. Set the `date` column as the DataFrame index.

  1. Drop the extra `date` column. (The index can now replace it.)

  1. Calculate daily returns.

  1. Use `loc()` to select subsets from the DatetimeIndex to create date ranges of 1, 2, 3, and 4 years. Remember that you can select date ranges using label indexing: `loc[start_date:end_date]`.

  1. Output summary statistics for each 1, 2, 3, and 4-year subset.

  1. Plot daily return charts for each 1, 2, 3, and 4-year subset.

  1. Formulate insights regarding the variation in average daily returns for each time period.

## Hint

Analyze the average daily returns from a numerical standpoint. Which time period has the highest average daily return and which has the lowest? What are the implications of this?

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
