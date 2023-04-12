/*

Sending Remittances
-------------------
In this activity, you’ll deploy and run the `CustomerAccount` contract that you created during the previous lesson to send remittances by using smart contracts.

Instructions
------------
1. Open the Remix IDE. Either paste the code from the starter file into a new Solidity file or open the `customer_account.sol` file that you created earlier.

2. Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

3. Navigate to the “Deploy & Run Transactions” pane, and then deploy your contract.

4. Run the `getInfo` function, and then review the output that the Remix IDE displays.

5. Use the `setInfo` function to fulfill the required customer information in the contract. Set an initial account balance of zero.

    **Note** You can either use the following Ethereum addresses or create new, dummy addresses on the Vanity-ETH website (https://vanity-eth.tk/), which includes an Ethereum vanity address generator. 

    Dummy owner address: 0x0c0669Cd5e60a6F4b8ce437E4a4A007093D368Cb
    Dummy authorized recipient address: 0x7A1f3dFAa0a4a19844B606CD6e91d693083B12c0

6. Run the `getInfo` function for a second time, and then review the output that the Remix IDE displays.

7. Use the `deposit` function to add 20 ether to the contract.

8. Run the `accountBalance` function, and then review the output that the Remix IDE displays.

    **Note** Did you notice anything interesting? You never coded a function named `accountBalance`. However, it’s available as a function for the deployed contract. 
    This is a getter function that the Solidity compiler automatically generated, because the `accountBalance` variable is public.

9. Use the `sendRemittance` function to send a remittance of 5 ether to either the account owner address or the authorized recipient address.

10. Run the `getInfo` function for the third time, and then review the output that the Remix IDE displays.

*/


pragma solidity ^0.5.0;

contract CustomerAccount {
    address payable owner;
    bool isNewAccount;
    uint public accountBalance;
    string customerName;
    string customerLastName;
    address payable authorizedRecipient;

    function getInfo() view public returns(address, address payable, bool, uint, string memory, string memory) {
        return (owner, authorizedRecipient, isNewAccount, accountBalance, customerName, customerLastName);
    }

    function setInfo(address payable newOwner, address payable newAuthorizedRecipient, bool newAccountStatus, uint newAccountBalance, string memory newCustomerName, string memory newCustomerLastName) public {
        owner = newOwner;
        authorizedRecipient = newAuthorizedRecipient;
        isNewAccount = newAccountStatus;
        accountBalance = newAccountBalance;
        customerName = newCustomerName;
        customerLastName = newCustomerLastName;
    }

    function sendRemittance(uint amount, address payable recipient) public {
        require(recipient == owner || recipient == authorizedRecipient, "The recipient address is not authorized!");
        recipient.transfer(amount);
        accountBalance = address(this).balance;
    }

    function deposit() public payable {
        accountBalance = address(this).balance;
    }

    function() external payable {}
}
