# Grouping By Columns in Pandas DataFrames

In this exercise you will learn how to group by specified columns to create aggregated subsets of data within Pandas DataFrames that can be used to calculate aggregated metrics.

## Instructions

Perform the following:

1. Import the `pandas` and `pathlib` libraries.

2. Create a variable `csvpath` that represents the path to the [cleaned_people_data.csv](Resources/cleaned_people_data.csv) using the Pathlib library.

3. Read the CSV into a Pandas DataFrame and display a few rows.

4. Use the `groupby` function to find the count of each `Occupation`.

5. Use the `groupby` function to find the mean of the `Salary` and `Age` of each `Occupation`.

6. Use the `groupby` function to find the mean of the `Salary` and `Age` of each `Occupation` and `Gender` combination.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
