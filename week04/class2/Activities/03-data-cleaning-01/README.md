# Cleaning Data in Pandas DataFrames

In this exercise you'll learn how to assess the quality of your data via the in-built functions Pandas provides for its DataFrames. Often times, data is rarely curated at the onset, therefore it is an important skill to know how to not only understand the quality of the data being used, but also how to fix the data quality errors.

## Instructions

1. Import the `pandas` and `pathlib` libraries.

2. Create a variable `csvpath` that represents the path to the [people_reordered.csv](Resources/people_reordered.csv) using the Pathlib library.

3. Read the CSV into a Pandas DataFrame and display a few rows.

4. View the column data types.

5. Drop the extraneous column `Unnamed: 0`.

6. Identify data quality issues:

    1. Identify the number of rows in the DataFrame.

    2. Identify the frequency counts of the `First_Name` column. This should identify the number of times a specific name occurs.

    3. Identify any null values in the DataFrame using the `isnull` function.

    4. Determine the number of nulls in the DataFrame using the `isnull` function in conjunction with the `sum` function.

    5. Determine the percentage of nulls for each column by chaining the `isnull` and `sum` functions then dividing by the `len` of the DataFrame. Multiply by `100` to produce a percentage rather than a decimal number.

    6. Check for duplicate rows using the `duplicated` function.

    7. Check for duplicate `first_name` and `last_name` values using the `duplicated` function.

7. Resolve data quality issues:

    1. Use the `fillna` function to fill `First_Name` and `Last_Name` values with the default value "Unnamed".

    2. Use the `dropna` function to drop the remaining records with nulls from the DataFrame. Use the `inplace` parameter set to `True` or resolve the changes to a new DataFrame.

    3. Check once more for null counts for each column.

    4. Use the `drop_duplicates` function with the `subset` parameter to drop duplicates based on the `Last_Name` and `First_Name` columns.

    5. Use the `as_type` function to convert the `Person_ID` column to the data type `int`.

8. Saved the cleansed data to a new CSV in the `Resources` folder.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
