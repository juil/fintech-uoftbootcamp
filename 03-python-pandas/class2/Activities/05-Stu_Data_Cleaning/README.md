# Spring Cleaning

It's that time of year again: the end of the fiscal year and the time to begin financial spring cleaning! Within a month, auditors will be camped out at your investment firm, inspecting everyone's trades and the company's end-of-year financial statements. All of the firm's traders are under a lot of pressure to finalize their portfolio earnings and deliver them to their managers. That is, all traders except you.

You automated your end-of-year financial reporting last week, and now you're using the pipeline to help Harold with his reports. Before loading Harold's stock ticker data into Pandas, you open the Excel file he sent you to look at the quality of the data. You realize that Harold has not subscribed to any data quality standards and that the data is a mess.

For this activity, use Pandas to clean Harold's portfolio data to get it fit for use.

## Instructions

Using the [starter file](Unsolved/spring_cleaning.ipynb) and Harold's financial [data](Resources/stock_data.csv), complete the following steps.

1. Load CSV data into Pandas using `read_csv`.

2. Identify the number of rows and columns in the DataFrame, otherwise known as its shape/structure.

3. Preview the DataFrame using `head` to visually ensure data has been loaded in correctly.

4. Identify the number of records in the DataFrame, and compare it with the number of rows in the original file.

5. Identify null records by calculating average percent of nulls for each Series. **Hint:** This step will require the `mean` function.

6. Drop null records.

7. Validate all nulls have been dropped by calculating the `sum` of values that are null.

8. Default null `ebitda` values to 0.

9. Check that there are no null `ebitda` values using the `sum` function.

10. Remove duplicate rows.

## Challenge

Now that nulls and duplicates have been wrangled, clean up the data a little more by removing the `$` currency symbols from the `price` field. Then, use the `astype` function to cast `price` to a `float`, and validate using `dtype`.

## Hint

Pandas offers a `replace` function that can be executed against a Series. Documentation can be found [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.replace.html).

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
