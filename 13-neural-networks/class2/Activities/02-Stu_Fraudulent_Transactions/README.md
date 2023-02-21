# Predicting Fraudulent Transactions Using Neural Networks

Now that you’ve learned how to build a deep neural network, you’ll apply those skills to create a deep learning model that can predict financial fraud. But in this activity, you will create a classification model instead of a regression model.

## Instructions

This activity is divided into two parts:

* Load and Preprocess the Data

* Create and Evaluate a Deep Neural Network Model

### Load and Preprocess the Data

1. Read the data from the CSV file into a Pandas DataFrame.

2. Create the target set `y` by assigning the values of the “isFraud” column of the DataFrame.

3. Define the features set `X` by including all the columns of the DataFrame except for the “isFraud” column.

4. Create the training and testing sets using the `train_test_split` function.

5. Scale the features data using StandardScaler.

### Create and Evaluate a Deep Neural Network Model

1. Create a deep neural network model with the following structure:

    * Nine inputs
    * First hidden layer with 18 neurons
    * Second hidden layer with eight neurons
    * Output layer with a single output
    * Hidden layers use the ReLU activation function and output layer uses the sigmoid activation function

2. Display the model structure using the 'summary` function.

3. Compile the neural network model using the `binary_crossentropy` loss function, the `adam` optimiser, and `accuracy` as an additional metric.

4. Fit the model with the training data for 100 epochs.

5. Evaluate the model using testing data and the `evaluate` method.

## References

[Keras Sequential model](https://keras.io/api/models/sequential/)

[Keras Dense module](https://keras.io/api/layers/core_layers/dense/)

[Keras evaluate](https://keras.io/api/models/model_training_apis/)

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
