# Student Do: Predicting Fraudulent Loan Applications

According to the American Bankers Association, [every dollar of fraud costs banks and credit unions roughly $2.92](https://www.aba.com/member-tools/industry-solutions/insights/state-card-fraud-2018). That's a reason why predicting fraud using machine learning techniques is a [broad area of research](https://scholar.google.com.mx/scholar?q=fraud+detection+machine+learning&btnG=&oq=fraud+detection+) and a great [business opportunity for FinTech startups](https://www.eu-startups.com/2019/06/paris-based-fintech-bleckwen-raises-e8-8-million-for-its-fraud-detection-software-to-prevent-financial-crime/).

In this activity, you will explore how tree-based algorithms can be used to identify fraudulent loan applications. You will start by using a decision tree model trained with the `sba_loans_encoded.csv` file that you created earlier.

## Instructions

### Loading and Preprocessing Loans Encoded Data

1. Load the `sba_loans_encoded.csv` in a Pandas DataFrame called `df_loans`.

2. Define the features set by copying the `df_loans` DataFrame and dropping the `Default` column.

3. Create the target vector by assigning the values of the `Default` column from the `df_loans` DataFrame.

4. Split the data into training and testing sets.

5. Use the `StandardScaler` to scale the features data; remember that only `X_train` and `X_testing` DataFrames should be scaled.

### Fitting the Decision Tree Model

6. Once data is scaled, create a decision tree instance and train it with the training data (`X_train_scaled` and `y_train`).

### Making Predictions Using the Tree Model

7. Validate the trained model by predicting fraudulent transactions using the testing data (`X_test_scaled`).

### Model Evaluation

8. Evaluate the model's results by using `sklearn` to calculate the confusion matrix and the accuracy score, and generate the classification report.

### Visualizing the Decision Tree

9. Create a visual representation of the decision tree using `pydotplus`. Show the graph on the notebook, and also save it in `PDF` and `PNG` formats.

### Analysis Question

10. Finally, analyze the model's evaluation results and answer the following question: Would you trust this model to deploy a loan application approval solution in a bank?

----

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.


