# Concatenating Pandas DataFrames

In this exercise you will learn how to concatenate DataFrames and append their data to a combined DataFrame.

## Instructions

Perform the following:

1. Import the `pandas` and `pathlib` libraries.

2. Create a two variables `msft_csv_path` and `sp500_csv_path` that represents the paths to the [MSFT.csv](Resources/MSFT.csv) and [SP500.csv](Resources/SP500.csv) using the Pathlib library.

3. Read the CSVs into two Pandas DataFrames.

4. Visualize the MSFT DataFrame.

5. Visualize the SP500 DataFrame.

6. Concatenate the `MSFT` and `SP500` DataFrames by columns using the `concat` function with the `axis` parameter set to `columns` and the `join` parameter set to `inner`.

7. Concatenate the `MSFT` and `SP500` DataFrames by rows using the `concat` function with the `axis` parameter set to `rows` and the `join` parameter set to `inner`.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
