# Financial Forecasting

In this activity, Harold's manager wants Harold to take a look at one year's worth of `TSLA` stock prices and plot a potential stock trajectory for where `TSLA` stock prices could go in the next `3` years. In addition, he would like to know how a $10,000 investment would perform given the simulated results.

Help Harold by creating a Monte Carlo simulation that simulates the next `252 * 3` trading days using three years worth of `TSLA` stock data. Plot the simulated results of `TSLA` daily returns over the next `3` years as well as the corresponding simulated outcomes.

## Instructions

Using the starter file provided, walk through the following steps.

* Import libraries and dependencies

* Use the `get_bars()` function to retrieve `3` year's worth of daily prices for `TSLA` stock as a `pandas` DataFrame.

* Build a Monte Carlo simulation that runs `1000` times through `252 * 3` trading days and saves the results.

* With these results, create a DataFrame which holds the mean, median, minimum, and maximum simulated cumulative return performance.

* Plot the simulated cumulative returns of `TSLA` stock over the next `3` trading years. Use only the `mean` and `median` cumulative returns over the simulations to produce this plot.

* Calculate the Simulated Profits/Losses of $10,000 Investment in `TSLA` Over the Next Three Years.

* Plot the simulated profits and losses for a $10,000 investment in TSLA given the simulated cumulative returns. For readability, use just the `mean` and `median` forecasts.

* Calculate the range of the possible outcomes of our $10,000 investments in `TSLA` stocks with a `95%` confidence interval.

## Hints

* Remember that a normal probability distribution is just a diagram illustrating the probability of potential outcomes as outcomes deviate closer to or away from the expected average.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
