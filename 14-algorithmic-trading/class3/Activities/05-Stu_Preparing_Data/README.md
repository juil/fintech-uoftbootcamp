# Preparing Data for a Machine Learning Trading Strategy

## Background

Before adding the power of machine learning into a trading algorithm, it's crucial to prepare the data that you will use to fit the model.

In this activity, you’ll prepare training and testing data for fitting a machine learning-powered trading algorithm.

## Instructions

1. Read the provided OHLCV data provided in the CSV file into a Pandas DataFrame.

    > **Hint:** Recall to set the `date` columns` as the DataFrame index and parse the dates.

2. Use the `pct_change` function to add a daily returns values column to the DataFrame. Name this column `actual_returns`.

    > **Hint:** Remove NAN values from the DataFrame.

3. Generate the features and target set as follows:

    * Set a short and long window size of 4 and 100 days, respectively and add the fast and slow, simple moving average columns to the DataFrame.

      > **Hint:** Remove NAN values from the DataFrame.

    * Create the features set by copying the `sma_fast` and `sma_slow` columns to a new DataFrame called `X`.

    * Add a `signal` column to the DataFrame setting its value to zeroes.

    * Use the Pandas `loc` function to populate the `signal` column as follows: where the `actual_returns` value is greater than or equal to zero, we set the `signal` value to 1. Where the `actual_returns` value is less than zero, we set the `signal` value to −1.

    * Create the target set `y` by copying the values of the `signal` column.

4. Split the data into training and testing sets as follows.

    * Use the pandas `DateOffset` module to set the beginning and end dates for the training the testing sets.

    * Set the `training_begin` date to the minimum date in the DataSet.

    * Set the ending period for the training data with an offset of 3 months

    * Use the `loc` function to generate the training datasets using the `training_begin` and `training_end` dates as lower and upper limits.

    * Create the testing sets using the `loc` function to slice the index starting at the `training_end` value and ending at the last record of the datasets.

5. Use the `StandardScaler` to standardise the training datasets.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
