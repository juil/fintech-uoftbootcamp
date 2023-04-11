# Adding Getters and Setters

## Instructions

1. Open the Remix IDE. Either paste the code from the starter file into a new Solidity file or open the `customer_contract.sol` file that you created earlier.

2. Create a `view public` getter function named `getInfo` that resembles the following:

    ```solidity
    function getInfo() view public returns() {
      // return user data here
    }
    ```

3. In `returns`, specify the types of data that the `getInfo` function will return. Then, write a return statement inside the body of the function that will return the values of all the variables that you specified before, such as `owner`, `isNewAccount`, `accountBalance`, `customerName`, and `customerLastName`.

    > **Hint** Remember to surround multiple return values with parentheses and to add the semicolons.

4. Because you no longer need the original default values for `owner`, `isNewAccount`, `accountBalance`, `customerName`, and `customerLastName`, remove them. (For example, change `bool isNewAccount = true;` to `bool isNewAccount;`.)

5. Create a setter function named `setInfo` that sets the values for `owner`, `isNewAccount`, `accountBalance`, `customerName`, and `customerLastName` and resembles the following:

    ```solidity

    function setInfo(address newOwner, bool newAccountStatus,
    uint newAccountBalance, string memory newCustomerName,
    string memory newCustomerLastName) public {
      // set user data here
    }
    ```

    > **Hint** Remember that the setter only sets the new values of the customer variables.

6. Compile the smart contract. If an error occurs, review the code, and make the necessary changes for a successful compilation.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
