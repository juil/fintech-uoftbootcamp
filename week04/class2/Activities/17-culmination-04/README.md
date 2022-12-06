# Gotta Catch em All: Listing the Strongest Pokemon

In this exercise, you will learn to bin records into separate groups through pandas. Namely, you will categorize the strongest pokemon and filter down to only those pokemon.

## Instructions

Perform the following:

1. Import the `pandas` and `pathlib` libraries.

2. Create a variable `pokemon_path` that represents the path to the [Pokemon.csv](Resources/Pokemon.csv) using the Pathlib library.

3. Import the CSV into a Pandas DataFrame named `pokemon_df`.

4. View summary statistics using the `describe` function.

5. Create bins for the future `Total Ranking` column: 'Very Weak', 'Weak', 'Moderate', 'Strong', 'Very Strong', 'Over Powered'.

6. Use the `cut` function to label each record based off of the `Total` column value and categorize each Pokemon into a corresponding `Total Ranking` bin.

7. Set the `Total Ranking` column as the index to the DataFrame.

8. Use `loc` to filter the DataFrame down to only the `Over Powered` Pokemon.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
