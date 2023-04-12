/*

Implement Ether Management Functions
------------------------------------
In this activity, you’ll extend the `CustomerAccount` contract that you created earlier by implementing functions that will allow you to send remittances and deposit ether.

Instructions
------------
1. Open the Remix IDE. Either paste the code from the starter file into a new Solidity file or open the `customer_account.sol` file that you created earlier.

2. Change the scope of the `accountBalance` variable to `public` to allow other users or contracts to access it. Specifically, making this variable public will allow both 
you and others to check the balance of ether in the contract when depositing or withdrawing ether.

3. Create a function named `sendRemittance`. Make this a withdrawing function that takes ether from the current contract balance. This function should accept a `uint` 
argument named `amount` and an `address payable` argument named `recipient`.

4. Inside the `sendRemittance` function, call the `transfer` method on the passed `recipient` argument, and specify the `amount` to transfer. Then declare an  `accountBalance` 
variable and set it equal to the balance of the contract. The body of the `sendRemittance` function should resemble the following:

    recipient.transfer(amount);
    accountBalance = address(this).balance;

**Note** In the preceding code, notice the `this` keyword. It refers to the smart contract itself. The `this` keyword helps you distinguish a contract's own balance from any
other balance.

5. Implement a `public payable` function named `deposit`. Inside this function, declare an  `accountBalance` variable and set it equal to the balance of the contract as follows:

    accountBalance = address(this).balance;

**Note** By declaring the `accountBalance` variable and setting it equal to the contract's balance inside both the `sendRemittance` and `deposit` functions, it can update the 
contract’s ether balance with each deposit or withdrawal.

6. Add the basic fallback function that we previously discussed so that the contract can store ether that’s sent from outside the `deposit` function.

7. Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

*/


pragma solidity ^0.5.0;

contract CustomerAccount {
    address owner;
    bool isNewAccount;
    uint accountBalance;
    string customerName;
    string customerLastName;

    function getInfo() view public returns(address, bool, uint, string memory, string memory) {
        return (owner, isNewAccount, accountBalance, customerName, customerLastName);
    }

    function setInfo(address newOwner, bool newAccountStatus, uint newAccountBalance, string memory newCustomerName, string memory newCustomerLastName) public {
        owner = newOwner;
        isNewAccount = newAccountStatus;
        accountBalance = newAccountBalance;
        customerName = newCustomerName;
        customerLastName = newCustomerLastName;
    }
}
