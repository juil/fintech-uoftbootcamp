# Diversification

Harold's company wants to build a diversified stock portfolio. So far, it has added `BMO` (Bank of Montreal) and `CNQ` (Canadian Natural Resources Limited), which reside within the financial services and energy sectors in [the S&P TSX 60 index](https://en.wikipedia.org/wiki/S%26P/TSX_60), respectively. Now they want to add a third energy sector stock to the mix.

Harold's manager wants him to research a set of five energy stocks to add to the existing portfolio. To create a diversified portfolio that tends to minimize long-term volatility/risk, stocks within the portfolio should be as uncorrelated as possible so as to create a counterbalance effect (i.e., when some stocks fall in price, others may rise in price).

Use the Pandas library to help Harold analyze five energy stocks—`CVE`, `ENB`, `IMO`, `IPL`, and `TRP`—and choose the stock with the least correlation to `BMO` and `CNQ`.

## Instructions

Using the [starter file](Unsolved/diversification.ipynb), complete the following steps:

1. Import libraries and dependencies.

2. Read in the following CSV files as Pandas DataFrames:

    * `CNQ.csv`
    * `BMO.csv`
    * `CVE.csv`
    * `ENB.csv`
    * `IMO.csv`
    * `IPL.csv`
    * `TSM.csv`

3. Use the `concat` function to combine the seven DataFrames into a single combined DataFrame with an index of `date`.

4. Calculate the daily returns using the `pct_change` function.

5. Use the `corr` function on the combined DataFrame to calculate and output a correlation table of each stock-to-stock pair.

6. From the correlation matrix, choose the stock with the least correlation to `BMO` and `CNQ` that should be added to the existing portfolio.

## Hint

Go [here](https://www.investopedia.com/terms/d/diversification.asp) to learn more about diversification and how correlation among stocks in portfolios are a factor in minimizing risk.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
