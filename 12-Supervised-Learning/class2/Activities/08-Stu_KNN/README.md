# KNN Bank Marketing Campaigns

In this activity, you will use the provided dataset of a bank's telemarketing campaign. The bank's marketing partner ran the campaign, and the bank has labelled the customers that opened an account after receiving a phone call. Now, they want you to build a model that will help them to provide the marketer with a better list of potential customers in the future.

## Instructions

1. Read the CSV file into a Pandas DataFrame.

2. Separate the features `X` from the target `y`.

3. Encode the categorical variables from the features data using [`get_dummies`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html).

4. Separate the data into training and testing subsets.

5. Scale the data using [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

6. Instantiate an k-nearest neighbour classifier instance.

7. Fit the model using the training data.

8. Make predictions using the testing data.

9. Generate the classification report for the test data.

## Hint

The column `y` is the target column.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
