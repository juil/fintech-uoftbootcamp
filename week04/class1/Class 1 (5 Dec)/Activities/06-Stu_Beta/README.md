# Beta Comparisons

Upper management at Harold's company is thinking about investing in a social media stock. They want to be somewhat conservative and look at social media stocks with the lowest beta relative to the others. Harold has been asked to calculate and plot the 30-day rolling betas for these social media stocks: Facebook (FB), Twitter (TWTR), and Snapchat (SNAP).

Use the Pandas library to help Harold calculate and plot the 30-day rolling betas for social media stocks, and then determine the social media stock with the lowest beta value.

## Instructions

Use the starter file to complete the following steps:

1. Import libraries and dependencies.

2. Read in the files `fb_data.csv`, `twtr_data.csv`, `snap_data.csv`, and `sp500_data.csv` as Pandas DataFrames. Set the Date column as a datetime index for each DataFrame.

3. Use `concat` to combine the DataFrames then sort the new DataFrame in ascending order.

4. Rename the columns to reflect the corresponding stock.

5. Use the `pct_change` function to calculate daily returns for each stock.

6. Calculate the overall covariances of each stock's daily returns to that of the S&P 500. Calculate the total variance of the S&P 500 daily returns.

7. Calculate the overall beta values of each social media stock.

8. Calculate the rolling 30-day covariances of each stock's daily returns to that of the S&P 500. Calculate the rolling 30-day variance of S&P 500 daily returns.

9. Calculate the rolling 30-day beta values of each social media stock.

10. Plot the rolling 30-day beta values of each social media stock on the same figure. Set the figure legend.

## Hint

Remember to set the `ax` parameter when plotting multiple datasets on a single chart figure.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
