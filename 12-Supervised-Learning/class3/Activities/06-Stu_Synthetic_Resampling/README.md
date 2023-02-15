# Improving Bank Marketing Campaigns with Synthetic Sampling

In this activity, you will use the provided dataset of a bank's telemarketing campaign. You will compare the effectiveness of synthetic resampling methods using a random forest. Then you will measure the random forest's recall of the minority class for both a random forest fitted to the resampled data and the original.

**Hint**: The column `y` is the target column.

## Instructions

1. Read the data into a Pandas DataFrame.

2. Separate the features `X` from the target `y`.

3. Encode the categorical variables from the features data using [`get_dummies`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html).

4. Separate the data into training and testing subsets.

5. Scale the data using [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

**RandomForestClassifier**

6. Create and fit a `RandomForestClassifier` to the **scaled** training data.

7.  Make predictions using the scaled testing data.

**Cluster Centroids**

8. Import `ClusterCentroids` from `imblearn`.

9. Fit the random undersampler to the scaled training data.

10. Check the `value_counts` for the resampled target.

11. Create and fit a `RandomForestClassifier` to the **resampled** training data.

12. Make predictions using the scaled testing data.

13. Generate and compare classification reports for each model.

**SMOTE**

14. Import `SMOTE` from `imblearn`.

15. Fit the random oversampler to the scaled training data.

16. Check the `value_counts` for the resampled target.

17. Create and fit a `RandomForestClassifier` to the **resampled** training data.

18. Make predictions using the scaled testing data.

19. Generate and compare classification reports for each model.

**SMOTEENN**

20. Import `SMOTEENN` from `imblearn`.

21. Fit the random oversampler to the scaled training data.

22. Check the `value_counts` for the resampled target.

23. Create and fit a `RandomForestClassifier` to the **resampled** training data.

24. Make predictions using the scaled testing data.

25. Generate and compare classification reports for each model.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.