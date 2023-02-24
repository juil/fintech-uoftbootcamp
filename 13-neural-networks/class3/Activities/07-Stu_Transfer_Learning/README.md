# Transfer Learning: Model Homes

In this activity, you’ll apply and customise a model to estimate property values in San Diego County, California.

## Background

Some real estate technology (or "proptech") companies like [Redfin](https://www.redfin.com/what-is-my-home-worth) or [Zillow](https://www.zillow.com/sellerlanding/pricingtool/) offer estimates of property value for almost every property in the United States.

But how do they know what any specific property is worth? The answer is that they feed the individual characteristics of any house into a pre-made model, with the output being the model's prediction of what that home is currently worth.

In this activity, your first task is to load a ready-made model built from modelling many thousands of different home prices in Los Angeles County, California. Then, you'll then apply this model to the smaller market for homes in San Diego County, California. Because these markets are similar but not identical, you'll also make adjustments to the model to customise it for the specifics of homes in San Diego County.

## Instructions

1. Load the model (`los_angeles_model.json`) and its weights (`los_angeles_model.h5`) from the Resources folder.

2. Use the `layers` attribute or `summary` function to count the number of layers.

3. Read in the San Diego County data (`san_diego.csv`, then `train_test_split` that data. The `y` variable should be `pricePerSquareFoot` and the `X` data should include `livingArea`,`bathrooms`,`bedrooms`,and `garageSpaces`.

4. Freeze the existing layers of the loaded model. Verify all layers are frozen by printing the `summary` of the model's architecture.

5. Create a new network which is an exact copy of this loaded model, but with the top layer from the original model removed.

6. Replace those removed layers with one or two new layers (including the final output layer). Ensure that these new trainable layers are added by using the `summary` function on this revised model.

7. Finally, compile and fit this newly revised model to the new data.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
