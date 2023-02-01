# Standardising and Clustering Currency Data

In this activity, you will use the K-means algorithm to segment global currency and interest rate data. Then you will evaluate the data by standardising and then segmenting the data into three clusters.

## Background

Almost every country around the world has its own currency and its own interest rate. In global markets, there is not one single interest rate used for borrowing and investing.

This naturally raises the question: Would it be possible to borrow in one currency, where interest rates are low, and invest it in another where interest rates are high? Doing so could yield a **spread**, or a profit difference, between the two interest rates. In fact, this strategy, called a **carry trade**, is common in international finance. [While not without risk](https://en.wikipedia.org/wiki/Carry_(investment)), carry trades can be a profitable way to further diversify an investment portfolio.

In this activity, you’ll use the `StandardScaler` module and clustering optimisation techniques to cluster global currencies and interest rates. The purpose of clustering the currencies will be to define which group of currencies offer the best currency carry.

## Instructions

1. Read in the `global_carry_trades.csv` file from the `Resources` folder and create and review the DataFrame. (This step is done for you in the starter code.)

2. To prepare the data, use the `StandardScaler` module and the `fit_transform` function to scale all the columns containing numerical values. Review a five-row sample of the scaled data using bracket notation ([0:5]).

3. Create a new DataFrame called `rate_df_scaled` that contains the scaled data. Make sure to do the following:

    * Use the same labels that were referenced in the `StandardScaler` for the column names.

    * Use `pd.get_dummies` on the "IMF Country Code" column on the original `rate_df` DataFrame. Save these binary variables as a DataFrame called `country_dummies`.

    * Use `pd.concat` to add the `country_dummies` DataFrame to the `rate_df_scaled` DataFrame. Display the combined DataFrame.

4. Fit the model and segment the data into clusters by using K-means.  Make sure to do the following:

    * Using the concatenated DataFrame, cluster the country level data by using the K-means algorithm and a `k` value of `3`. Save the predicted model clusters to a new DataFrame.

    * Create a copy of the `rate_df_scaled` DataFrame, saving it to a new DataFrame called `rate_scaled_predictions`. Add the predicted `country_clusters` to this new DataFrame, then preview its content.

5. Plot and analyse the results. Make sure to do the following:

    * Group the saved DataFrame by cluster using `groupby`. Plot average `next_month_currency_return` by cluster to identify which group had the highest monthly currency returns.

    * Use `hvplot` to create a scatter plot of `interest_differential` against `next_month_currency_return`, making the plot vary by `CountryCluster`.

    * Based on this plot, which country cluster appears to provide both the highest interest spread and currency return?

### Optional Challenge

For an extra challenge, do the following:

* Use `AgglomerativeClustering`, `BIRCH`, or any number of the [other clustering methods available on scikit-learn](https://scikit-learn.org/stable/modules/clustering.html#overview-of-clustering-methods) and re-estimate clusters on the DataFrame you created in the main part of this activity.

* Increase the cluster count to determine whether there are any smaller, more granular clusters that show the most potential for profit.

## References

* [scikit-learn StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

* [scikit-learn preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-scaler)

* [Pandas concat function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)

* [scikit-learn Python library](https://scikit-learn.org)

—--

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
