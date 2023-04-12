# Deploying and Testing a Personal Savings Smart Contract

In this activity, you will extend the functionality of the personal savings smart contract that you were working on in today's class. After coding the updates requested, you will compile the contract; next, you will deploy and test the contract's functions in the Remix IDE local blockchain.

## Instructions

Open the [Remix IDE](http://remix.ethereum.org/) and eithre import the `PersonalSavings.sol` starter file or copy and paste its contents into the Remix IDE, then complete the following steps:

1. Modify the `PersonalSavings` contract to initialize the following variables:

    * An address variable `last_to_withdraw`.

    * A unsigned integer variable `last_withdraw_amount`.

    * An address variable `last_to_deposit`.

    * A unsigned integer variable `last_deposit_amount`.

    * A public unsigned integer variable `balance`.

2. Modify the `withdraw` function in the `PersonalSavings` contract as follows:

    * Replace the `if` statement for two `require` function calls as follows:

      * The first `require` function call should check if the recipient address is the public or private saving address. 
      If the function returns false, the error message `This is not your account` will be risen.

      * The second `require` function call should check if there is enough Ether in the contract balance to commit 
      the withdrawal operation. If the function returns false, the error message `You don't have enough funds!` will be risen.

    * Use an `if` statement to check if the `last_to_withdraw` is NOT equal to `recipient`. If it isn't, set `last_to_withdraw` 
    equal to `recipient`.

    * Set `last_withdraw_amount` equal to the `amount` parameter.

    * Update the `balance` variable to the current contract balance minus the amount that was withdrawn.

3. Modify the `deposit` function in the `PersonalSavings` contract as follows:

    * Use an `if` statement to check if the `last_to_deposit` is NOT equal to `msg.sender`.
    If it isn't, set `last_to_deposit` equal to `msg.sender`.

    * Set `last_deposit_amount` equal to the `msg.value` variable.

    * Set `balance` equal to the current contract.

4. Compile the contract and fix any existing bugs.

5. After a successful compilation, deploy the contract on the JavaScript VM provide by the Remix IDE.

6. Test the contract's functions as follows:

    * Deposit 10 Ether to the contract.

    * Use the `balance` getter function to corroborate that the current balance of the contract is 10 Ether (10000000000000000000 Wei).

      > **Hint:** You can use this [Etherium Unit Converter](https://eth-converter.com) to convert between ether and wei.

    * Use the `withdraw` function to transfer 1 Ether to the private savings address. Recall that transfers should be expressed in Wei.

    * Use the `balance` getter function to corroborate that the current balance of the contract is 9 Ether (9000000000000000000 Wei).

    * Use the `withdraw` function to transfer 1 Ether to the following invalid address: `0xd83F8A76e7F699669Fe85C5Da2F7f09907A15a53`. 
    Verify that the error defined in the `require` function is risen.

    * Use the `withdraw` function to transfer 15 Ether to the public savings address. Since you there are not enough fund in the contract, 
    corroborate that that the error defined in the `require` function is risen.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
