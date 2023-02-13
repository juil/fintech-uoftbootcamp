# Credit Card Fraud

In this activity, you will practice resampling techniques and use different models to classify credit card transactions as fraudulent or not fraudulent. 

## Instructions

* Implement one oversampling, one undersampling, and one combination sampling technique using the algorithm of your choice. 

* For each sampling technique, fit a logistic regression model to the resulting resampled data and print the imbalanced classification report.

* Fit an ensemble method of your choosing to the training data. Examples of ensemble methods include `GradientBoostingTree`, `XGBoost` and `RandomForest`.

* Choose the logistic regression model that has the "best" results from the resampled data.

* Using a Precision Recall Curve, compare the chosen logistic regression model results to the results of your chosen ensemble method.


## Hints:

* You may need to increase the number of maximum training iterations in the logistic regression model. This can be set using the `max_iter` parameter.

```
model = LogisticRegression(solver='lbfgs', random_state=1, max_iter=2000)
```

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
