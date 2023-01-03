# Indexing Fever

You've caught the multi-indexing fever! Add power to your financial analytic pipelines by indexing your data by month and year with a DatetimeIndex.

For this demo, you will use historical stock data from [Bombardier (BBD.B)](https://web.tmxmoney.com/quote.php?qm_symbol=BBD.B) that comprises `BBD.B` ticker prices from March to May 2019.

## Instructions

Use the starter file to complete the following steps:

1. Use `read_csv` to load the CSV data into a Pandas DataFrame called `bbd_df`.

2. In the `read_csv` function, set the index to equal the `Date` series. Enable the  `parse_dates` and `infer_datetime_format` parameters.

3. Assess and clean the data.

4. Group data by DatetimeIndex year and month.

5. Select close price for `BBD.B` for May 2019 by passing in values for `year` and `month` indices.

### Challenge

Take this activity to the next level by calculating the mean close price for `BBD.B` for all of `2019`.

### Hints

* Additional information about `DatetimeIndex` capabilities can be found [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html).

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
