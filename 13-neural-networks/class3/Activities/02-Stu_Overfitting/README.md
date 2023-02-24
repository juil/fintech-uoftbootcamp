# Insurtech: Categorical Risk

In this activity, you will build a deep neural network that uses personal characteristics to quantify insurance claims.

## Background

The insurance business revolves around quantifying risk: the insurer invests insurance premiums in financial markets and makes payouts in the form of insurance claims. Both investments and claims payouts require models to quantify and predict risk, or the level of potential financial loss.

This dataset contains historical claims payouts for medical insurance buyers and their characteristics (age, smoker/non-smoker, etc.). Can you build a deep neural network that uses people's characteristics to quantify the potential level of dollar claims? Can you make your model robust to overfitting?

## Instructions

This activity is divided into two main parts:

* Prepare the data

* Fit the model

### Prepare the Data

1. Read in the data.

2. Use `pd.qcut` to split the dependent variable, `charges`, into five categorical buckets. Save this result to a `charges_quantile` column.

3. Use `LabelEncoder` and `to_categorical` to set this column as your `y` variable.

4. Set the remaining data as your `X` data.

5. Split the data into training and test windows using `train_test_split`.

### Fit the Model

1. Fit and evaluate the model. Include at least one dropout layer and one layer with regularisation. Include a validation set as part of fitting the model.

2. Plot performance on the training and validation set across epochs.

3. Finally, re-fit the new model, adjusting the amount of epochs for training to avoid overfitting as much as possible.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
