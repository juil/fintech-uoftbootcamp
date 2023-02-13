# Predicting with Logistic Regression

## Background

In this scenario, you work for a strategic consulting firm focusing on financial services. You've been contacted by a company that is trying to predict fraudulent transactions that occur on its payment system. You tell them that you have the tools to help them with their classification problem, and they send you a dataset.

## Files

* [predicting_fraudulent_transactions.ipynb (Unsolved)](Unsolved/predicting_fraudulent_transactions.ipynb)

* [transaction_fraud_data.csv](Resources/transaction_fraud_data.csv)

Use the Jupyter notebook file in the `Unsolved` folder to write your code. The `Resources` folder contains the CSV file that you’ll import.

## Instructions

The instructions for this activity are divided into the following stages:

1. Prepare the data.

2. Split the data into training and testing sets.

3. Model and fit the data into a logistic regression.

4. Predict the testing labels.

5. Calculate the performance metrics.

#### Prepare the Data

1. Load the `transaction_fraud_data.csv` file from the `Resources` folder into a Pandas DataFrame. Set the “id” column as the index.

2. Note that you want to predict the `fraud` variable. Answer the following question: Using `value_counts`, how many fraudulent transactions exist in this dataset?

#### Split the Data into Training and Testing Sets

1. Using the `transaction_fraud_data` DataFrame, separate the data into training and testing data. Start by defining the `target` (the “fraud” column) and the `features` of the data (all the columns except “fraud”).

2. Split the features and target data into `training_features`, `testing_features`, `training_targets`, and `testing_targets` datasets by using the `train_test_split` function.

#### Model and Fit the Data to a Logistic Regression

1. Declare a `LogisticRegression` model.

2. Fit the training data to the model, and then save the model.

#### Predict the Testing Labels

1. Make predictions about fraud by using the testing dataset, and save those predictions.

#### Calculate the Performance Metrics

1. Calculate the accuracy score by evaluating `testing_targets` vs. `testing_predictions`.

2. Answer the following question: For this dataset, how well did the model predict the truly fraudulent transactions?

## Resources

Visit the following links for information on the scikit-learn modules that you need for this activity:

[logistic regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

[train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

[accuracy score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)

[classification report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
