# Standardising Stock Data

In this activity, you will use the K-means algorithm to segment customer data for mobile versus in-person banking service ratings. Before you’re able to cluster the data, you’ll need to preprocess it by using the techniques that you've learned in this lesson.

## Instructions

1. Read in the `tsx-energy-2018.csv` file from the `Resources` folder and create the DataFrame. Make sure to set the Ticker column as the DataFrame’s index. Then review the DataFrame.

   > **Note** The stock data that’s provided for this activity contains the yearly mean prices (open, high, low, and close), volume, annual return, and annual variance from companies in the energy sector that the TSX lists.

2. To prepare the data, use the `StandardScaler` module and the `fit_transform` function to scale all the columns containing numerical values. Review a five-row sample of the scaled data using bracket notation ([0:5]).

3. Create a new DataFrame called `df_stocks_scaled` that contains the scaled data. Make sure to do the following:

   * Use the same labels that were referenced in the `StandardScaler` for the column names.

   * Add a column to the DataFrame that consists of the tickers from the original DataFrame. (Hint: This column was the index).

   * Set the new column of tickers as the index for the new DataFrame.

   * Review the resulting DataFrame.

4. Encode the “EnergyType” column using `pd.get_dummies`, and save the result in a separate DataFrame called `df_oil_dummies`. Note that because the company name isn’t relevant for clustering, you don’t need to encode the “CompanyName” column.

5. Using the `pd.concat` function, concatenate the `df_stocks_scaled` DataFrame with the `df_oil_dummies` DataFrame, along an axis value of 1 (`axis=1` tells Pandas to join the data horizontally by columns). Review the concatenated DataFrame.

6. Using the concatenated DataFrame, cluster the data by using the K-means algorithm and a k value of 3. Create a copy of the concatenated DataFrame, and add the resulting list of company segment values as a new column.

--—

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
