# Enforcing Contract Terms

In this activity, you’ll use the `require` function to enhance the `sendRemittance` function of the `CustomerAccount` contract that you created in an earlier lesson.

## Background

You’ve already added functionality to the `CustomerAccount` smart contract that allows a user to send remittances. Now, you want to make sure that only the owner or an authorized recipient can receive remittances. This rule will serve to avoid unauthorized transactions. You'll thus enhance the `sendRemittances` function by using `require`.

## Instructions

1. Open the Remix IDE. Either paste the code from the starter file, `customer_account.sol`, into a new Solidity file or open the `customer_account.sol` file that you created earlier.

2. Define an `address payable` variable named `authorizedRecipient`. This Ethereum address will represent a third-party account that’s authorized to receive withdrawal payments.

3. To allow the account owner to receive withdrawal payments at their Ethereum address, change the `owner` variable to become `payable`.

4. Modify the type of the `newOwner` variable in the `setInfo` function to `address payable`. This will avoid compilation errors from the change that you made to the `owner` variable.

5. Change the `sendRemittance` function by adding a `require` function. This `require` function will enforce the rule that only the account owner or the authorized recipient can receive ether from the contract balance.

6. Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
