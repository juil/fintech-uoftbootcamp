# Market Analysis

In this activity, Harold has been asked to analyze the financial data of the companies in the S&P 500. Specifically, Harold has been asked to find and plot the following:

1. A pie chart of the S&P 500 company sector distribution.

2. A bar chart of the top 20 market cap companies.

3. A scatter plot of the price vs. earnings relationship.

Use the Pandas library to help Harold perform this analysis and generate the plots.

## Instructions

Use the starter Jupyter notebook to complete the following steps.

1. Import the necessary libraries and dependencies.

2. Read in the `sp500_companies.csv` as a Pandas DataFrame.

3. Use the `value_counts()` function on the `Sector` column of the DataFrame to count and return a Series object representing the frequency of unique values.

4. Plot a pie chart of the S&P 500 company sector distribution.

5. Create a subset DataFrame by selecting the `Symbol` and `Market Cap` columns. Use the `nlargest()` function on the subset DataFrame to return the top 20 rows of the `Market Cap` column.

6. Plot a bar chart of the top 20 market cap companies.

7. Create a subset DataFrame by selecting the `Price` and `Earnings/Share` columns.

8. Plot a scatter plot of the price vs. earnings/share relationship.

## Hints

* Consult the [Pandas documentation](https://pandas.pydata.org/pandas-docs/version/0.17.0/index.html) for more information about the `value_counts()` and `nlargest()` functions.

* In the [Pandas Visualization help document](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html) you can learn more about the different kinds of plots that Pandas supports.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
