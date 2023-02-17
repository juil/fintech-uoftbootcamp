# Preventing Credit Card Defaults with Neural Networks, Part 1

In this activity, you will train a neural network model to predict whether a credit card holder will default in the next month.

The dataset provided contains 30,000 anonymous records of credit default status. There are 23 features columns and one binary target column named DEFAULT, where 1 represents a defaulted credit card.

The 23 features include demographic information (age, gender, marital status, etc.), credit limit, past payment details, and other relevant information.

Your task is to create a neural network model that can predict if a credit card holder will default.

## Instructions

1. Load the data in a Pandas DataFrame.

2. Define the features set `X` by including all the columns of the DataFrame except the DEFAULT column.

3. Create the target vector `y` by assigning the values of the DEFAULT column of the DataFrame.

4. Create the training and testing sets using the `train_test_split` function from sklearn.

5. Scale the features data using the StandardScaler from sklearn.

6. Create a neural network model with 22 inputs, one hidden layer with 12 units, and an output layer with a single output. Use the ReLU activation function for the first layer and the sigmoid function for the second layer.

7. Display the model structure using the `summary` function.

## References

[Keras Sequential model](https://keras.io/api/models/sequential/)

[Keras Dense module](https://keras.io/api/layers/core_layers/dense/)

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.