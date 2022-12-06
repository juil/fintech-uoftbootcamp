# Binning Data in Pandas DataFrames

In this exercise you'll learn how to categorize records in Pandas DataFrames using a specified numerical column value that will be used to evaluate the category in which the record should be placed.

## Instructions

Perform the following:

1. Import the `pandas` and `pathlib` libraries.

2. Create a variable `csvpath` that represents the path to the [cleaned_people_data.csv](Resources/cleaned_people_data.csv) using the Pathlib library.

3. Read the CSV into a Pandas DataFrame.

4. Create bins from 0, 30000, 70000, 100000, and 200000. Set the bin names as 'Low', 'Moderate', 'Above Average', and 'High', respectively.

5. Use the `cut` function to slice the DataFrame by the specified bins and append the bin names as a new column `Salary Level`.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
