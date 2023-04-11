# Travel Expenses Contract

## Background

You work for a fintech company that offers accounting services to small- and medium-sized businesses. The first application that your company launched uses a smart contract to keep track of travel expenses.

In this activity, you will practice variable declarations, and basic math and assignation operations in Solidity by creating a travel expenses smart contract. You will complete the code for the `TravelExpenses` contract and it's `RecordExpense` function.

## Instructions

Open the [Remix IDE](http://remix.ethereum.org/), import the starter file (`TravelExpenses.sol`), and then complete the following steps:

1. Create a `public payable address` variable named `corporate_account`, and assign a valid Ethereum address to it.

2. Create a `payable address` variable named `personal_account`, and assign a valid Ethereum address to it.

3. Define a `string` variable named `employee_name`, and assign your name to it.

4. Create a 256-bit unsigned integer constant named `daily_expenses_eth` that has a value of 1.

5. Create a 256-bit unsigned integer variable named `current_expenses_wei` that has an initial value of 0.

6. Create an unsigned integer variable named `current_taxes_wei` that has an initial value of 0.

7. Create a 16-bit unsigned integer variable named `expenses_count` that has an initial value of 0.

8. Create a 32-bit unsigned integer variable named `eth_usd_rate`, and assign it the current value in USD of 1 ETH.

9. Create a 256-bit unsigned integer constant named `eth_wei_rate`, and assign it the the number of wei in one ether.

10. Create a `public` 256-bit unsigned integer variable named `daily_expenses_wei`, and assign it the value of `daily_expenses_eth` times `eth_wei_rate`.

11. Create a 256-bit unsigned integer variable named `expense_usd_no_tax`, and assign it the value of `new_net_expense_usd` minus the taxes.

12. Create a 256-bit unsigned integer variable named `taxes_usd`, and assign it the taxes in USD from `new_net_expense_usd`.

13. Update `current_expenses_wei` by adding `expense_usd_no_tax` converted to wei.

14. Update `current_taxes_wei` by adding the `taxes_usd` converted to wei.

15. Increase `expenses_count` by one unit.

16. Compile the file to ensure that the code works.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
