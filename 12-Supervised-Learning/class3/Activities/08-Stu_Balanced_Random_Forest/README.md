# Activity: Comparing Imbalanced Classifiers

In this activity, you’ll fit various balanced and imbalanced models to small-business loan data. You’ll then compare the results by using the metrics that you’ve learned.

## Overview

The U.S. Small Business Administration (SBA) is a government agency that supports the creation and growth of small companies through numerous activities including grants and loan guarantees. A guarantee means that the SBA will repay to the lender a percentage of the remaining balance if the business defaults on the loan.

The dataset for this activity contains information about actual small business loans that the SBA has guaranteed. This dataset contains the following columns:

- “Year”: The fiscal year of the loan application.

- “Month”: The month of the fiscal year.

- “Amount”: The issued loan amount.

- “Term”: The term of the loan, in months.

- “Zip”: The borrower’s ZIP code.

- “CreateJob”: The number of jobs that were created by using the loan.

- “NoEmp”: The number of business employees.

- “RealEstate”: Whether the loan is backed by real estate.

- “RevLineCr”: Whether the loan is a revolving line of credit.

- “UrbanRural”: The location type of the borrower.

- “Default”: Whether the borrower defaulted on the loan (1) or not (0).

This dataset is imbalanced. Failure to repay a loan (that is, when the “Default” value equals 1) occurred rarely compared to the number of loans that borrowers successfully repaid.

Using some of these variables as features, you'll need to try various models to assess those that can best predict which SBA loans are most likely to default.

## Files

Use the Jupyter notebook file in the `Unsolved` folder to write your code. The `Resources` folder contains the CSV file that you’ll import.

## Instructions

1. Read in the CSV file from the `Resources` folder into a Pandas DataFrame.

2. Create a Series named `y` that contains the data from the "Default" column of the original DataFrame. Note that this Series will contain the labels. Create a new DataFrame named `X` that contains the remaining columns from the original DataFrame. Note that this DataFrame will contain the features.

3. Split the features and labels into training and testing sets, and use `StandardScaler` on your `X` data.

4. Check the magnitude of imbalance in the dataset by viewing the number of distinct values (`value_counts`) for the labels. 

5. Fit two versions of a random forest model to the data: the first, a regular `RandomForest` classifier, and the second, a `BalancedRandomForest` classifier.

6. Resample and fit the training data by using one additional method for imbalanced data, such as `RandomOverSampler`, undersampling, or a synthetic technique.

7. Print the confusion matrixes, accuracy scores, and classification reports for the three different models.

8. Evaluate the effectiveness of `RandomForest`, `BalancedRandomForest`, and your selected additional imbalanced classifier for predicting the minority class.

  * Answer the following question: Does the model generated using one of the resampled classifiers more accurately flag all the loans that eventually defaulted?

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.