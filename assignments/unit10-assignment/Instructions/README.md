# Module 10 Challenge: Crypto Clustering

![Decorative image.](Images/10-5-challenge-image.png)

## Background

In this Challenge, you’ll assume the role of an advisor at one of the top five financial advisory firms in the world. Competitors are fierce, so you want to propose a novel approach to assembling investment portfolios that are based on cryptocurrencies. Instead of basing your proposal on only returns and volatility, you want to include other factors that might impact the crypto market&mdash;leading to better performance for your portfolio.

When you present the idea, your manager loves it! So, you’re asked to create a prototype for submitting your crypto portfolio proposal to the company board of directors.

## What You're Creating

In this Challenge, you’ll combine your financial Python programming skills with the new unsupervised learning skills that you acquired in this module.

You’ll create a Jupyter notebook that clusters cryptocurrencies by their performance in different time periods. You’ll then plot the results so that you can visually show the performance to the board.

The CSV file that’s provided for this Homework contains the price change data of cryptocurrencies in different periods.

## Files

Download the following files to help you get started:

[Module 10 Challenge files](Starter_Code)

## Instructions

Use the starter code file to complete the tasks outlined in the Instructions. The steps for this assignment are divided into the following sections:

* Import the Data (provided in the starter code)

* Prepare the Data (provided in the starter code)

* Find the Best Value for k Using the Original Data

* Cluster Cryptocurrencies with K-means Using the Original Data

* Optimise Clusters with Principal Component Analysis

* Find the Best Value for k Using the PCA Data

* Cluster the Cryptocurrencies with K-means Using the PCA Data

* Visualise and Compare the Results

> **Note:** For the purpose of this assignment, assume that k refers to lowercase k. The instructions will specify "uppercase K" where necessary.

### Find the Best Value for k Using the Original Data

In this section, you will use the elbow method to find the best value for k.

1. Code the elbow method algorithm to find the best value for k. Use a range from 1 to 11.

2. Plot a line chart with all the inertia values computed with the different values of k to visually identify the optimal value for k.

3. Answer the following question: What is the best value for k?

### Cluster Cryptocurrencies with K-means Using the Original Data

In this section, you will use the K-means algorithm with the best value for k (found in the previous section) in order to cluster the cryptocurrencies according to the price changes of cryptocurrencies provided.

1. Initialize the K-means model with four clusters by using the best value for k.

2. Fit the K-means model using the original data.

3. Predict the clusters to group the cryptocurrencies using the original data. View the resulting array of cluster values.

4. Create a copy of the original data and add a new column with the predicted clusters.

5. Using hvPlot, create a scatter plot by setting `x="price_change_percentage_24h"` and `y="price_change_percentage_7d"`. Colour the graph points with the labels found using K-means. Then, add the crypto name in the `hover_cols` parameter to identify the cryptocurrency represented by each data point.

### Optimise Clusters with Principal Component Analysis

In this section, you will perform a principal component analysis (PCA) and reduce the features to three principal components.

1. Create a PCA model instance and set `n_components=3`.

2. Use the PCA model to reduce to three principal components. View the first five rows of the DataFrame.

3. Retrieve the explained variance to determine how much information can be attributed to each principal component.

4. Answer the following question: What is the total explained variance of the three principal components?

5. Create a new DataFrame with the PCA data. Be sure to set the `coin_id` index from the original DataFrame as the index for the new DataFrame. Review the resulting DataFrame.

### Find the Best Value for k Using the PCA Data

In this section, you will use the elbow method to find the best value for k by using the PCA data.

1. Code the elbow method algorithm and use the PCA data to find the best value for k. Use a range from 1 to 11.

2. Plot a line chart with all the inertia values computed with the different values of k to visually identify the optimal value for k.

3. Answer the following questions: What is the best value for k when using the PCA data? Does it differ from the best k value found using the original data?

### Cluster Cryptocurrencies with K-means Using the PCA Data

In this section, you will use the PCA data and the K-means algorithm with the best value for k (found in the previous section) in order to cluster the cryptocurrencies according to the principal components.

1. Initialize the K-means model with four clusters by using the best value for k.

2. Fit the K-means model by using the PCA data.

3. Predict the clusters to group the cryptocurrencies by using the PCA data. View the resulting array of cluster values.

4. Create a copy of the DataFrame with the PCA data and add a new column to store the predicted clusters.

5. Using hvPlot, create a scatter plot by setting `x="PC1"` and `y="PC2"`. Colour the graph points with the labels found using K-means. Then, add the crypto name in the `hover_cols` parameter to identify the cryptocurrency represented by each data point.

### Visualise and Compare the Results

In this section, you will visually analyse the cluster analysis results by observing the outcome with and without using the optimisation techniques.

1. Create a composite plot using hvPlot and the plus (`+`) operator to compare the elbow curve that you created to find the best value for k with the original data and the PCA data.

2. Create a composite plot using hvPlot and the plus (`+`) operator to compare the cryptocurrencies clusters using the original data and the PCA data.

3. Answer the following question: After visually analysing the cluster analysis results, what is the impact of using fewer features to cluster the data by using K-means?

> **Hint** Recall that you learned how to create composite plots in Module 6. Review that module if you need a refresher on making these plots. You can also check [the hvPlot documentation](https://holoviz.org/tutorial/Composing_Plots.html).

### Requirements

#### Find the Best Value for k Using the Original Data (15 points)

##### To receive all points, you must

* Code the elbow method algorithm to find the best value for k. Use a range from 1 to 11. (5 points)

* Plot a line chart with all the inertia values computed with the different values of k to visually identify the optimal value for k. (5 points)

* Answer the following question: What is the best value for k? (5 points)

#### Cluster Cryptocurrencies with K-means Using the Original Data (10 points)

##### To receive all points, you must

* Initialize the K-means model with four clusters by using the best value for k. (1 point)

* Fit the K-means model by using the original data. (1 point)

* Predict the clusters to group the cryptocurrencies using the original data. View the resulting array of cluster values. (3 points)

* Create a copy of the original data and add a new column with the predicted clusters. (1 point)

* Using hvPlot, create a scatter plot by setting `x="price_change_percentage_24h"` and `y="price_change_percentage_7d"`. Colour the graph points with the labels found by using K-means. Then, add the crypto name in the `hover_cols` parameter to identify the cryptocurrency represented by each data point. (4 points)

#### Optimize Clusters with Principal Component Analysis (10 points)

##### To receive all points, you must

* Create a PCA model instance and set `n_components=3`. (1 point)

* Use the PCA model to reduce to three principal components. View the first five rows of the DataFrame. (2 points)

* Retrieve the explained variance to determine how much information can be attributed to each principal component. (2 points)

* Answer the following question: What is the total explained variance of the three principal components? (3 points)

* Create a new DataFrame with the PCA data. Be sure to set the `coin_id` index from the original DataFrame as the index for the new DataFrame. Review the resulting DataFrame. (2 points)

#### Find the Best Value for k Using the PCA Data (10 points)

##### To receive all points, you must

* Code the elbow method algorithm and use the PCA data to find the best value for k. Use a range from 1 to 11. (2 points)

* Plot a line chart with all the inertia values computed with the different values of k to visually identify the optimal value for k. (5 points)

* Answer the following questions: What is the best value for k when using the PCA data? Does it differ from the best k value found by using the original data? (3 points)

#### Cluster Cryptocurrencies with K-means Using the PCA Data (10 points)

##### To receive all points, you must

* Initialize the K-means model with four clusters by using the best value for k. (1 point)

* Fit the K-means model using the PCA data. (1 point)

* Predict the clusters to group the cryptocurrencies using the PCA data. View the resulting array of cluster values. (3 points)

* Create a copy of the DataFrame with the PCA data and add a new column to store the predicted clusters. (1 point)

* Using hvPlot, create a scatter plot by setting `x="PC1"` and `y="PC2"`. Colour the graph points with the labels found by using K-means. Then, add the crypto name in the `over_cols` parameter to identify the cryptocurrency represented by each data point. (4 points)

#### Visualise and Compare the Results (15 points)

##### To receive all points, you must

* Create a composite plot using hvPlot and the plus (`+`) operator to compare the elbow curve that you created to find the best value for k with the original data and the PCA data. (5 points)

* Create a composite plot using hvPlot and the plus (`+`) operator to compare the cryptocurrencies clusters using the original data and the PCA data. (5 points)

* Answer the following question: After visually analysing the cluster analysis results, what is the impact of using fewer features to cluster the data using K-means? (5 points)

#### Coding Conventions and Formatting (10 points)

##### To receive all points, you must

* Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. (3 points)

* Name functions and variables with lowercase characters, with words separated by underscores. (2 points)

* Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. (3 points)

* Use concise logic and creative engineering where possible. (2 points)

#### Deployment and Submission (10 points)

##### To receive all points, you must

* Submit a link to a GitHub repository that’s cloned to your local machine and contains your files. (4 points)

* Use the command line to add your files the repository. (3 points)

* Include appropriate commit messages in your files. (3 points)

#### Code Comments (10 points)

##### To receive all points, your code must

* Be well commented with concise, relevant notes that other developers can understand. (10 points)

### Submission

To submit your Challenge assignment, click Submit, and then provide the URL of your GitHub repository for grading.

> **Note** You are allowed to miss up to two Challenge assignments and still earn your certificate. If you complete all Challenge assignments, your lowest two grades will be dropped. If you wish to skip this assignment, click Submit, and then indicate you are skipping by typing “I choose to skip this assignment” in the text box.

Comments are disabled for graded submissions in BootCamp Spot. If you have questions about your feedback, please notify your instructional staff or your Student Success Manager. If you would like to resubmit your work for an improved grade, you can use the Resubmit Assignment button to upload new links. You may resubmit up to three times for a total of four submissions.

---

Copyright 2022 2U. All Rights Reserved.
