# Foreign Keys

In this activity, you will create and populate two new tables with foreign keys that reference existing data.

## Instructions

Complete the following:

* Create a database called `estate_db`.

* Use the provided CSV files to create and populate the `owners` and `estates` tables:

  * [owners.csv](Resources/owners.csv)

  * [estates.csv](Resources/estates.csv)

* Make sure that the `estates` table contains an `owner_id` foreign key that references the `owner_id` column in the `owners` table.

* Test foreign keys by writing a query to insert data in the `estates` table that does not have a reference ID in the `owners` table.

* Join the two tables.

## Hint

Think about how you can select certain columns in a table. Use those columns as a reference to insert data into a table.

## Bonus

* Use the provided CSV files to create two new tables - `estate_type` and `estates_new`:

  * [estate_type.csv](Resources/estate_type.csv)

  * [estates_new.csv](Resources/estates_new.csv)

* Make sure that the `estates_new` table contains an `estate_type_id` foreign key that references the `estate_type_id` column in the `estate_type` table.

* Join all three `owners`, `estates_new`, and `estate_type` tables together.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
