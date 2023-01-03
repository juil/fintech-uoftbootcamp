# Risky Business

Harold has been involved in some risky business. He's gotten serious about the cryptocurrency market, and has seen some excellent returns. Harold's latest returns have him strutting around the office like he's the world's best trader. He even had the audacity to bet you five dollars that his portfolio returns are better than yours!

Using standard deviation and Sharpe ratios, do the following:

* Identify which cryptocurrencies have the greatest risk-to-reward ratio.

* Determine which portfolio (yours or Harold's) has made the most smart investments.

* Identify which cryptocurrencies have the greatest Sharpe ratios (risk/reward).

## Instructions

Use the starter file and the provided data to complete the following steps:

1. Load CSV data into Pandas using `read_csv` for each file and remove any null values using `dropna`.

2. Prepare the data by dropping null values and setting `Date` as the index.

2. Calculate daily returns for each portfolio.

3. Concat both DataFrames containing daily returns into one DataFrame.

4. Calculate standard deviation for the combined DataFrame.

5. Calculate the Sharpe ratios by computing the quotient of `annualized average return` and `annualized standard deviation`.

6. Plot the Sharpe ratios using a bar chart.

7. Answer the following questions:

    * How many smart investments did Harold make compared to risky investments? How many did you make?

    * Which cryptos have been the smartest investments?

### Challenge

Calculate the Sharpe ratio for your entire portfolio. Then, use a comparison operator to see which portfolio has the greatest risk-to-reward ratio.

1. Calculate annualized `std dev` for each portfolio.

2. Calculate the Sharpe ratios for each crypto in each portfolio.

3. Average the Sharpe ratios calculated in the previous step.

    **Hint:** `harold_sharpe_ratios.mean()`

4. Determine if Harold's portfolio's Sharpe ratio average is greater than your own.

    **Hint:** Use a comparison operator to compare Sharpe ratio averages.

5. Determine which portfolio is the smartest investment based on the risk-to-reward ratio.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
