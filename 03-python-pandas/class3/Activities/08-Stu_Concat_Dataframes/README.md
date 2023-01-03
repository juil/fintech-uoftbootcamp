# Mastering Concatenation

Two county organizations that you are a part of, Financial Leaders of America and Investors Leadership Council, have recently joined forces.

Eager to consolidate the dues and membership data, the treasurer has reached out to you––the group's FinTech guru––to create a master ledger containing financial data for both organizations.

Help the treasurer out by consolidating the dues and member data.

## Instructions

Use the starter file and the data provided to complete the following steps:

1. Load CSV data into Pandas using `read_csv` for each file.

2. Concatenate dues. Use the `concat` function to concatenate the `fin_leaders_america.csv` data with the `invstrs_leadership.csv` data by `axis='rows'` and `join='inner'`.

3. Concatenate member data. Use the `concat` function to concatenate the `fin_leaders_members.csv` data and the `invstrs_leadership_members.csv` data by `axis='columns'` and `join='inner'`.

4. Concatenate dues and member data. Use the `concat` function to concatenate the two DataFrames made in steps 2 and 3 using by `axis='columns'` and `join='inner'`.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
