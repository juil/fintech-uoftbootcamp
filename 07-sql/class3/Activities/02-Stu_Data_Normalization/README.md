# Employee Normalizer

In this activity, you will be organizing improperly stored employee data into the three normal forms.

## Instructions

* In pgAdmin, create a new database called `normalization_db`.

* Create a new table `employee_normalization` according to the provided [employee_normalization.csv](Resources/employee_normalization.csv), then import the csv into the `employee_normalization` table.

* Create a new table `first_nf_employee` that organizes the data in `employee_normalization` according to first normal form standards.

* Then, create two new tables `second_nf_employee` and `second_nf_employee_email` that organize the data in `first_nf_employee` according to second normal form standards.

* Lastly, create two new tables `third_nf_employee` and `third_nf_zipcode` that organize the data in `second_nf_employee` according to third normal form standards.

### Bonus

* Join the `third_nf_employee`, `second_nf_employee_email` and `third_nf_zipcode` tables to re-create the initial dataset.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
