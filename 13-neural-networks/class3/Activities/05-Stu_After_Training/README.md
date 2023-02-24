# After Training

In this activity, you will create a deep learning model from the credit score data, save the model, and load it to evaluate its performance on unseen data.

## Instructions

1. Split the data into training and test sets using the `train_test_split` method. Scale the features data using an instance of the `StandardScaler`.

2. Using the training set for your data, construct a shallow neural network model to predict the credit score features. You can create a new model or use the model from the previous credit scoring activity.

3. Using relative file paths, save the model and its weights.

4. Load the model and its weights.

5. Use this loaded model to predict points for the test data and print the mean squared error (MSE) metric for the predicted points vs. the actual points.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.