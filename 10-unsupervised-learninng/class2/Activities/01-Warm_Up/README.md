# Clustering National Home Markets

In this activity, you will use the K-means algorithm to identify trends within a dataset of residential house prices in the US.

## Background

You work for a large national bank with a large lending business that provides loans to people who want to buy homes in the United States. The bank wants to have a model that can identify how similar the national real estate market is at any point in time in comparison to real estate periods in the past. Quantifying today's real estate market against the past will help the bank better understand its lending risk as well as the potential for new growth.

You've decided to use the K-means algorithm to segment different periods in the U.S. market for national residential house prices.

Using the information in the [starter file](Unsolved/homebuying_eras.ipynb), apply the K-means algorithm to the lending data using both three and four clusters to segment the national home sales trends.

## Instructions

1. Review the Pandas DataFrame and plot associated with `national-home-sales.csv`.

2. Run the K-means algorithm identifying three clusters in the data. To do so, complete these steps:

   * Create and initialise the K-means model for three clusters. Use a `random_state` value of 1 for the model.

   * Fit, or train, the model by using the `home_sales_df` DataFrame.

   * Make predictions about the clustering by using the trained model. Save the predictions to a variable called `home_segment_3`, and print that variable.

   * Create a copy of the DataFrame and name it `home_sales_predictions_df`.

   * Add a column to the `home_sales_predictions_df` DataFrame called "home_segment_3", and add the `home_segment_3` information to the column.

   * Plot the data by using the DataFrame adjusted to include home market segment information for three clusters.

3. Run the K-means algorithm identifying four clusters in the data. To do so, complete these steps:

   * Create and initialise the K-means model for four clusters. Use a `random_state` value of 1 for the model.

   * Fit, or train, the model by using the `home_sales_df` DataFrame.

   * Make predictions about the clustering by using the trained model. Save the predictions to a variable called `home_segment_4`, and print that variable.

   * Add a column to the `home_sales_predictions_df` DataFrame called "customer_segment_4", and add the `home_segment_4` information to the column.

   * Plot the data by using the DataFrame adjusted to include customer segment information for four clusters.

4. Answer the following question: Can any additional information be gleaned from the customer segmentation data when clusters of three and four are applied?

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
