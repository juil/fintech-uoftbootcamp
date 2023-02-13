# Evaluating Classification Models

It's your turn to evaluate how a logistic regression model performs. In this activity, you are working to help a fintech startup more quickly grow its user base. By doing so, you’ll discover how machine learning has the potential to turbocharge the growth trajectory of a fintech firm.

## Background

**Snowballing** is a business growth strategy that is based on the fact that the social networks of individuals tend to have certain characteristics in common. This has implications for a fintech startup that wants to expand its product to more customers. If you can identify your best customers, you can use them to snowball your product to more, but similarly great, new customers.

While you don’t yet have many customers, you’ve done a good job of collecting data about their usage statistics. Specifically, you have data about the following:

* What you want to predict:

  * “Target”, which indicates whether a customer has referred your product to a new customer and whether both now heavily use the product. (If this is true, y equals 1.)

* What you will use to generate predictions for the preceding column:

  * "Usage Stats”, which is a metric that tracks how frequently the customer engages with the product.

  * “Referral History”, which relates to how frequently the customer has referred your product to others in the past.

  * “Customer Rank”, which is a financial score that measures how profitable this customer has been.

You’ve been tasked with using this data to build a model that can predict which customers will likely be the best referrers for new customers. How well will your model classify these snowball customers?

## Files

Use the Jupyter notebook file in the `Unsolved` folder to write your code. The `Resources` folder contains the CSV file that you’ll import.

## Instructions

1. Read in the dataset about the current customers of the startup.

2. Split the data into X and y and then into testing and training sets.

3. Fit a logistic regression classifier.

4. Create the predicted values for the testing and the training data.

5. Print a confusion matrix for the training data.

6. Print a confusion matrix for the testing data.

7. Print the training classification report.

8. Print the testing classification report.

9. Answer the following question: How does the model performance comparison between the training data and the testing data?

## Resources

Visit the following links for information on the scikit-learn modules needed for this activity:

[logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

[train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

[classifiction_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)

[confusion_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
