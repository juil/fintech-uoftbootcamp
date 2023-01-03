# World Happiness

In this exercise we will be looking at the World Happiness report for 2017. It includes the happiness score of every country in relation to various contributing factors such as economic production (GDP) and life expectancy. This is a chance to use what you have learned in class so far and get more practice working with pandas. You are expected to be able to sort and filter the data based on given parameters. This exercise will go over...

* Setting a new index for the dataframe
* Navigating through dataframes using `loc` and `iloc`
* Locating a specific data value
* Filtering and slicing specific rows of data
* Creating new tables based on specific columns
* Filtering data based on a specific condition
* Filtering data based on multiple conditions

The data set for this is actually quite interesting. Does money buy happiness? Do happy people live longer? I guess you'll find that out and more! Good luck and have fun with this one!

## Instructions

Perform the following:

1. Import the `pandas` and pathlib libraries.

2. Create a variable `csv_path` that represents the path to the [world_happiness.csv](Resources/world_happiness.csv) using the Pathlib library.

3. Import the CSV into a Pandas DataFrame.

4. Set the `Country` column as the index and sort the index in ascending order.

5. Select the `Happiness.Score` for 'Vietnam' using loc.

6. Select the `Happiness.Rank` and `Happiness.Score` for 'Belgium', 'Belize', 'Benin', 'Bhutan', and 'Bolivia'.

7. Select the `Freedom` and `Trust..Government.Corruption.` columns for each row/country.

8. Select the countries where the `Economy..GDP.per.Capita` is greater than or equal to 1.6 using the loc function.

9. Select the countries where the `Happiness.Score` is greater than or equal to 5, and `Economy..GDP.per.Capita` is less than or equal to 1.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
