# Segmenting Customer Data

In this activity, you will use BIRCH, agglomerative clustering, and the K-means model to segment a dataset on thousands of consumer credit card holders. Then you’ll compare the results of the three different clustering methods.

## Background

One of the world's biggest banks launched a machine learning competition in [Kaggle](https://www.kaggle.com/), an online community of data scientists and machine learning practitioners. The bank wants to improve their marketing campaigns by identifying the optimal number of customer segments for their credit card clients, and are offering $5,000 in prize money to the winner. The cash prize has piqued your interest, so you have decided to put your hat in the ring and your unsupervised learning skills into practice!

The bank provided a dataset that consists of customer data that includes 10 different features. The data columns were anonymised using generic names to protect customers' privacy, and data values were already normalised.

## Instructions

Use the [starter file](Unsolved/segmenting_customer_data.ipynb) to accomplish the following tasks:

1. Load the raw data into a Pandas DataFrame.

2. Use the elbow method to determine the optimal number of clusters.

3. Segment the data with K-means, using the optimal number of clusters.

4. Cluster the data by using agglomerative clustering and BIRCH.

    * Using the optimal number of clusters found in Step 2, estimate clusters by using both `AgglomerativeClustering` and `Birch`. Save each of these models and their results for comparison.

5. Compare the cluster results from using K-means, agglomerative clustering, and BIRCH.  Make sure to do the following:

    * Create a DataFrame which is a copy of the original `customers_df` data.

    * Add all of the predicted labels (`kmeans_predictions`, `agglo_predictions`, and `birch_predictions`) as columns to this DataFrame.

    * For each algorithm, plot the clusters by using the "feature_1" and "feature_2" columns.

### Optional Challenge

Loop through each clustering algorithm, using an alternative metric to determine the optimal number of clusters. To do so, follow these steps:

1. Create three lists (or a dictionary or DataFrame) to contain the metrics to measure optimal clusters.

2. Using a `for` loop, cycle through a list of cluster counts, fitting each of the three clustering algorithms.

3. When fitting the clustering algorithms in the loop, estimate the [variance ratio criterion (Calinski-Harabasz index)`](https://scikit-learn.org/stable/modules/clustering.html#calinski-harabasz-index) and save that metric to your metrics lists in (1).

    > **Hint:** Code samples for these and other metrics can be found in scikit-learn documentation on [clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation).

4. Output each of the three lists. If larger metric values indicate a better number of clusters, what cluster count is best? Does it vary by the algorithm selected?

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
