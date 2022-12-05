# Simple Moving Averages

Harold's manager wants him to plot the 20-day, 50-day, and 100-day simple moving averages and rolling standard deviations for Shopify Inc. stock (`SHOP`). Upper management is considering a long-term investment in `SHOP`, but they want to ensure they are making a move at the right time.

Use the Pandas library to help Harold plot the simple moving averages and rolling standard deviations to generate insights into whether `SHOP` is worth a long-term investment.

## Instructions

Use the starter file to complete the following steps:

1. Import libraries and dependencies.

2. Read in `shop.csv` as a Pandas DataFrame, and set the Date column as a datetime index, then plot the data. stan

3. Use the `rolling` function and set the `window` parameter to designate the time windows. Then, use the `mean` function to calculate the following:

    * 20-day simple moving average

    * 50-day simple moving average

    * 100-day simple moving average

4. Overlay the plot for daily closing prices of `SHOP` with the SMAs.

5. Perform the same actions from items 3 and 4, only this time calculate the rolling standard deviation by using the `std` function instead of `mean`.  Try chaining the functions to create the calculation and the plot in one line.  Example: `df.rolling(window=20).std().plot(ax=ax)`.

## Hint

Go [here](https://www.investopedia.com/terms/s/sma.asp) to learn more about simple moving averages and how they work.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
