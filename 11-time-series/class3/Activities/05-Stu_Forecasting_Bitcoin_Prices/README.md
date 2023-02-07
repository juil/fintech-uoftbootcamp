# Forecasting Bitcoin Prices by Using Prophet

In this activity, you’ll use Prophet to forecast prices of Bitcoin.

## Background

In this scenario, you are working as a financial advisor. Your most important client has asked you to invest 10% of their monthly retirement fund allocation in Bitcoin.

You decide to analyse the patterns for hourly Bitcoin prices. By building a model that can forecast prices into the future, you should get an idea of whether investing in Bitcoin is worthwhile.

## Instructions

Load the starter notebook into Google Colab and complete the following steps:

1. Execute the code cells under the "Notebook Set Up" section.

2. Read in the `bitcoin_hourly` CSV file. Drop the `volume` column.

3. Label the columns `ds` and `y` so that the syntax is recognised by Prophet.

4. View the DataFrame shape, and the first and last five rows of the DataFrame.

5. Sort the DataFrame by `ds` in ascending order, which arranges the data chronologically from past to present. Then, visually inspect the price data using `hvplot`.

6. Call the `Prophet` function, and store it as an object.

7. `Fit` the time-series model.

8. Create a `future_trends` dataframe to hold predictions, using the `make_future_dataframe` function. (Make the prediction go out as far as 1,000 hours).

9. Make the predictions for the trend data using the `future_trends` DataFrame, and preview the first five rows of the DataFrame.

10. Plot the Prophet predictions for the `forecast_trends` data.

11. Use the `plot_components` function to visualise the forecast results.

12. Set the `datetime` index of the `forecast_trends` data, using the `ds` column.

13. From the `forecast_trends` DataFrame, use `hvPlot` to visualise the `yhat`, `yhat_lower`, and `yhat_upper` columns over the last 10 days (i.e., the last 240 rows).

14. Create a `forecast_march_2021` Dataframe, which contains just forecasts for that month (March). The DataFrame should include the columns `yhat_upper`, `yhat_lower`, and `yhat`. Replace the column names with names that are easier to understand: `Best Case`, `Worst Case`, and `Most Likely Case`, respectively.

15. Display the average forecasted price for March 2021

    **Hint:** You can use the [Pandas `mean` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html).

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
