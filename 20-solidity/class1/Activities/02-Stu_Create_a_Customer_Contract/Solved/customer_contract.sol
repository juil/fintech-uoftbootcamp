/*

Create a Customer Contract
--------------------------
In this activity, you’ll create a smart contract by using Solidity to store customer information.

Instructions
------------
1. Create a basic smart contract named `CustomerAccount`. To do so, use the following starter code:

    pragma solidity ^0.5.0;

    contract CustomerAccount {
    // insert code here
    }

2. Create the following variables in the body of the smart contract, and use the appropriate data type for each:

    * The `owner` variable: Holds the Ethereum address of the main customer (for example, 0xaaaaaaaaaaaaaaaaa).

    * The `isNewAccount` variable: Represents whether the account is new (that is, `true` or `false`).

    * The `accountBalance` variable: Holds the account balance (for example, 10000).

    * The `customerName` variable: Holds the first name of the customer (for example, "Jordan").

    * The `customerLastName` variable: Holds the last name of the customer (for example, "Habib").

3. Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

*/


pragma solidity ^0.5.0;

contract CustomerAccount {
    address owner = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
    bool isNewAccount = true;
    uint accountBalance = 10000;
    string customerName = "Jordan";
    string customerLastName = "Habib";
}
