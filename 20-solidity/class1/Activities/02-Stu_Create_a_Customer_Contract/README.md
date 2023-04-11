# Create a Customer Contract

## Background

Year after year, immigrants in the United States send billions of dollars to support their families who are living in their home countries/regions. These people use several methods to send the money. But, they use remittance providers, like Western Union, the most frequently.

As a fintech professional, you realize that this presents a potential market for using blockchain technology. Specifically, people will potentially be able to send money all over the world by using cryptocurrencies and paying lower commissions.

The first step is to create a smart contract that stores the customer information.

## Instructions

1. Create a basic smart contract named `CustomerAccount`. To do so, use the following starter code:

    ```Solidity
    pragma solidity ^0.5.0;

    contract CustomerAccount {
    // insert code here
    }
    ```

2. Create the following variables in the body of the smart contract, and use the appropriate data type for each:

    * The `owner` variable: Holds the Ethereum address (for example, 0xaaaaaaaaaaaaaaaaa) of the main customer.

    * The `isNewAccount` variable: Represents whether the account is new (that is, it contains `true` or `false`).

    * The `accountBalance` variable: Holds the account balance (for example, 10000).

    * The `customerName` variable: Holds the first name of the customer (for example, "Jordan").

    * The `customerLastName` variable: Holds the last name of the customer (for example, "Habib").

3. Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
