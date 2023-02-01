# Energise Your Stock Clustering

In this activity, you’ll use the K-means algorithm and clustering optimisation techniques to cluster stocks. The purpose will be to define a portfolio investment strategy.

## Instructions

1. Read in the `tsx-energy-2018.csv` file from the `Resources` folder and create the DataFrame. Make sure to set the `Ticker` column as the DataFrame’s index. Then review the DataFrame.

    > **Note:** This step has been completed for you. Be sure to run these cells before moving on to Step 2.

2. Review the four code cells that are included in this step in the notebook. These cells contain the code that scales the `df_stocks` DataFrame and creates a new DataFrame that contains the scaled data.

    > **Note:** This step has been completed for you. Be sure to run these cells before moving on to Step 3.

3. Using the `df_stocks_scaled` DataFrame, cluster the data by using the K-means algorithm and a lowercase-k value of 3. Add the resulting list of company segment values as a new column in the `df_stocks_scaled` DataFrame.

    > **Hint:** You can use a lowercase-k value of 3 to start, or you can use the elbow method to find the optimal value for lowercase-k.

4. Using hvPlot, create a scatter plot to visualize the clusters setting `x="AnnualVariance"`,  `y="Annual Return"`, and `by="StockCluster"`. Be sure to style and format your plot.

    > *Hint:** Remember that you can style your plot using hvPlot’s customisation parameters. For example, you can add the ticker symbol to the tooltip of each point by using hvPlot’s `hover_cols` parameter. For a refresher on customising `hvplot`, refer to [Customization](https://hvplot.holoviz.org/user_guide/Customization.html) in the hvPlot user guide.

5. To get another perspective on the clusters, reduce the number of features to two principal components by using PCA. Make sure to do the following:

    * Use the `df_stocks_scaled` DataFrame to complete this analysis.

    * Review the PCA data.

    * Calculate the explained variance ratio that results from the PCA data.

6. Using the PCA data calculated in the previous step, create a new DataFrame called `df_stocks_pca`. Make sure to do the following:

    * Add an additional column to the DataFrame that contains the tickers from the original `df_stocks` DataFrame.

    * Set the new Tickers column as the index.

    * Review the DataFrame.

7. Rerun the K-means algorithm with the new principal-components data, and then create a scatter plot by using the two principal components for the x and y axes, and by using `StockCluster`. Be sure to style and format your plot.

### Optional Challenge

Find the best `k` with `PCA`. Make sure to do the following:

* Code the elbow method algorithm and use the PCA data to find the best value for k. Use a range from 1 to 11.

* Plot a line chart with all the inertia values computed with the different values of k to visually identify the optimal value for k.

* Answer the following question: What is the best value for k when using the PCA data? Does it differ from the best k value found using the original data?

## References

* [scikit-learn PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

* [scikit-learn StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

* [scikit-learn preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-scaler)

* [scikit-learn Python library](https://scikit-learn.org)

* [hvPlot customization](https://hvplot.holoviz.org/user_guide/Customization.html)

—--

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
