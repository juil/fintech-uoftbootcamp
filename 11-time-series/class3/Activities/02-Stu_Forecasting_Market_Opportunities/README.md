# Assessing Market Opportunities for Alpaca Wool Scarves: Time Series Forecasting

In this activity, you’ll use time series forecasting to analyse Google Trends data. The purpose will be to validate market opportunities to help the Aymara indigenous people in Bolivia export alpaca wool scarves to different countries or regions.

You’ll continue collaborating with the International Co-operative Alliance. But now, you’ll use Prophet to validate prospective market opportunities.

## Instructions

1. Open [Google Colab](https://colab.research.google.com/), and then import the provided notebook.

2. Run the code cells in "Step 2" to set up and prepare the data.

3. Create two Prophet models, one for each country.

4. Fit the Prophet models.

5. Use the `make_future_dataframe` function to forecast one year of trend dates.

   **Hint:** Google Trends data is collected weekly. So, set the `freq` parameter to `W`, and set `periods=52` (because one year has 52 weeks).

6. Predict the future trends data by using the `predict` function for both the Canada and Uruguay models.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
