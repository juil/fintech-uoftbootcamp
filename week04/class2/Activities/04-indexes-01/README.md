# Slice and Dice Pandas DataFrames via Indexes

In this exercise you'll learn how to use indexes to select specific portions (via rows and columns) of a Pandas DataFrame.

## Instructions

Perform the following:

1. Import the `pandas` and `pathlib` libraries.

2. Create a variable `csvpath` that represents the path to the [cleaned_people_data.csv](Resources/cleaned_people_data.csv) using the Pathlib library.

3. Read the CSV into a Pandas DataFrame and display a few rows.

4. Index Selection with `iloc`:

    1. Select the first row of the DataFrame using `iloc`.

    2. Select the first 10 rows of the DataFrame using `iloc`.

    3. Select the last row of the DataFrame using `iloc`.

    4. Select the second column using `iloc`.

    5. Select the last column using `iloc`.

    6. Select the first three columns using `iloc`.

    7. Select the 1st, 3rd, 5th, and 7th rows of the 2nd, 4th, and 6th columns using `iloc`.

    8. Select the first 5 rows of the 3rd, 4th, and 5th columns using `iloc`.

    9. Modify the `first_name` column value of the first row using `get_loc` and `iloc`.

5. Index Selection with `loc`:

    1. Set the `First_Name` column as the Pandas DataFrame index.

    2. Sort the DataFrame by the `First_Name` index in ascending order.

    3. Select the row with the `First_Name` index "Andrew" using `loc`.

    4. Select the rows between 'Andrew' and 'Vonnie' using `loc`.

    5. Select the rows where `Gender` is equal to 'Male' using `loc`.

    6. Change the `First_Name` value of the rows with 'Aaron' as the `First_Name` index to 'Arod'.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
