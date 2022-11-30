# Reading Stock Data from a CSV File

Now that you learned how easy it is to work with spreadsheet data in Pandas, let's practice using some real financial data! In this activity, you will create a DataFrame from a CSV file and then explore its contents using the DataFrame's built-in functions.

## Instructions

Using the starter file, complete the following steps.

1. Import the Pandas library by initializing the program with `import pandas as pd`.

2. Create a DataFrame by reading in the `shopify_stock_data.csv` file containing historical price data for [Shopify](https://www.shopify.com/) from 2015 to 2019 at the Toronto Stock Exchange.

3. Perform an initial data exploration by getting the top `10` rows of the DataFrame.

4. Oh no! There are no column names on the DataFrame. Fix this problem by recreating the DataFrame and setting the column names to "Date", "Close", "Volume", "Open", "High", "Low".

5. When the column names are fixed, get the first `10` rows from the DataFrame.

## Challenge

Get the bottom `10` rows of the DataFrame. Use Google to figure out how to do this.

## Hint

Consult the Pandas [`head()` function documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html).

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
