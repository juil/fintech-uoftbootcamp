# Game of Thrones: Pandas Are Coming

In this exercise we will be analyzing character deaths in Game of Thrones. **WARNING** If you watch the show and are not caught up you may be spoiled!

You will be able to flex your newly found pandas skills and masterfully navigate and filter through the dataset. Specific to this exercise you will get practice with...

* Creating a new table from the existing dataset
* Grouping data based on a specific column
* Sorting the data and reseting the index
* Filtering data based on multiple conditions

This exercise is meant to be somewhat challenging. If you get stuck look to your in-class activities! Some of the more challenging parts might require methods that have not been covered yet or only briefly touched on, so practice your Google-Fu and start looking things up!

## Instructions

Perform the following:

1. Import the `pandas` and pathlib libraries.

2. Create a variable `got_path` that represents the path to the [game_of_thrones.csv](Resources/game_of_thrones.csv) using the Pathlib library.

3. Import the CSV into a Pandas DataFrame

4. Use the `unique` function to count the unique `Allegiances`.

5. Filter and create another DataFrame that only contains the `Allegiances` and `Name` columns.

6. Groupby the `Allegiances` column and count the number of members for each `Allegiance`.

7. Rename the `Name` column to `Members` for the DataFrame containing allegiance counts.

8. Sort the DataFrame by the `Members` column in descending order.

9. Select the 2nd largest allegiance via `iloc`.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
