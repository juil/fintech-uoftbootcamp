# Three-Year Loans

The higher-ups at Harold's firm want to know how to better target customers who are seeking three-year loans. Harold's manager has asked him to review a compilation of loan data, and then filter out the necessary data to generate insights about customers who have been granted three-year loans.

Follow the instructions to help Harold answer his manager's questions.

## Instructions

Complete the following steps.

1. Import the necessary libraries and dependencies.

2. Read in the `loans.csv` data into a Pandas DataFrame.

3. Show the first `10` records of the data.

4. View summary statistics for the `loans.csv` data.

5. Create a subset DataFrame `filtered_df` by filtering the columns so that only the following columns remain:

    * `loan_amnt`
    * `term`
    * `int_rate`
    * `emp_title`
    * `annual_inc`
    * `purpose`

6. Filter `filtered_df` by row values where `term` is equal to `36 months` in order to focus on three-year loan records only.

7. Modify rows with `term` values equal to `36 months` to be `3 years`.

8. Use the `isnull()` function to modify rows with `emp_title` values equal to `NaN` to be `Unknown`.

9. View summary statistics for `term_df` after all modifications.

10. Use the `value_counts()` function on the `emp_title` column of the `term_df` DataFrame to see the unique value counts for employee titles of three-year loan customers.

11. Use the `value_counts()` function on the `purpose` column of the `term_df` DataFrame to see the unique value counts for loan purposes of three-year loan customers.

12. Filter `term_df` by rows with `annual_inc` greater than `80000`. Use the `mean()` function to see the average `int_rate` of three-year loan customers with annual incomes greater than $80,000.

13. Filter `term_df` by rows with `annual_inc` less than `80000`. Use the `mean()` function to see the average `int_rate` of three-year loan customers with annual incomes less than $80,000.

14. Help Harold answer the following questions for his manager:

    * What kind of customers (employee title) seem to ask for three-year loans most frequently?

    * What are three-year loans generally used for?

    * What is the difference between counts of three-year loan customers with annual incomes greater than `$80,000`, compared to those with annual incomes less than `$80,000`?

    * What is the difference between interest rates for customers with annual incomes greater than `$80,000` compared to those with annual incomes less than `$80,000`?

## Hint

View the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/) for additional explanations about using specific functions.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
