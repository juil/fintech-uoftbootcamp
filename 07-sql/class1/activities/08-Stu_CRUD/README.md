# Using CRUD: CREATE, READ, UPDATE, and DELETE

In this activity, you will be utilizing CRUD operations (Create, Read, Update, Delete) on the provided data.

## Instructions

* Create a new database named `sales_db` in pgAdmin.

* Create a table `sales` and define the correct column names and data types according to the `sales.csv`. Import the data from `sales.csv` using the pgAdmin Import/Export tool.

* Create a query to return the sales records with loan amounts less than $300,000.

* Create a query to find the [average](https://www.w3schools.com/sql/sql_count_avg_sum.asp) loan amount of all the sales records.

* Update the loan amount for sales_id 33 to $423,212.

* Add a new boolean column `loan_distributed` that defaults to True.

* Insert a new record into the sales table where the sales_id is 101, the payment_id is 101, the mortgage_id is 2, the loan_amount is $734,544, and the loan_date is `1995-10-05`.

* Delete the sales record where sales_id is 72.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
