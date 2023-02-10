# Student Do: Encoding Categorical Data for Machine Learning

In this activity, you are tasked with encoding some categorical and text features of a dataset that contains 2,097 loan applications. In later activities, you will use this dataset to predict fraudulent transactions.

## Dataset Description

The data provided is based on the dataset used in the research paper titled [“Should This Loan be Approved or Denied?”: A Large Dataset with Class Assignment Guidelines](https://doi.org/10.1080/10691898.2018.1434342), published by Min Li, Amy Mickel, and Stanley Taylor of  California State University in the Journal of Statistics Education.

This dataset contains information about loans applications managed by the US Small Business Administration (SBA), and was adapted for today's class. The dataset is distributed under the [Creative Commons (CC BY-SA 4.0) license](https://creativecommons.org/licenses/by-sa/4.0/).

The columns in the dataset are as follow:

* `Year`: The fiscal year of the loan application
* `Month`: Month of the fiscal year
* `Amount`: The loan amount issued
* `Term`: The loan's term (in months)
* `Bank`: Name of the bank issuing the loan
* `State`: Borrower state
* `City`: Borrower city
* `Zip`: Borrower zip code
* `CreateJob`: Number of jobs created using the loan
* `NoEmp`: Number of business employees
* `RealEstate`: Defines if loan is backed by real estate
* `RevLineCr`: Indicates if the loan is a revolving line of credit
* `UrbanRural`: Location type of the borrower
* `Default`: Indicates if the loan was defaulted on (`1`) or not (`0`)

## Instructions

### Loading the Data

Load the `sba_loans.csv` data in a Pandas DataFame. Show the `head` to get familiar with the columns and data values.

### Integer Encoding

#### Manual Integer Encoding

Perform a manual integer encoding of the `Month` column; use a dictionary to map months' names with their corresponding numerical value.

#### Encoding Data using `LabelEncoder`

Use the `LabelEncoder` method from `sklearn` to perform an integer encoding of the `RealEstate`, `RevLineCr`, and `UrbanRural` columns.

#### Encoding Data using `get_dummies()`

Perform a binary encoding on the `Bank`, `State`, and `City` columns using the Pandas `get_dummies()` function.

### Save the Preprocessed File

Finally, save the preprocessed file as `sba_loans_encoded.csv` for forthcoming usage.

## Hints

You can use the Pythons' [`calendar` module](https://docs.python.org/3/library/calendar.html) to create the months dictionary for the manual integer encoding of the `month` column, as explained [here](https://stackoverflow.com/a/31796820/4325668).

https://www.aba.com/member-tools/industry-solutions/insights/state-card-fraud-2018

----

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.

