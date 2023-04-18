# SafeMath

In this activity, you’ll incorporate the SafeMath library into the `ArcadeToken` smart contract. To secure your token, you’ll then use SafeMath functions for all the math operations in the contract.

## Instructions

1. Navigate to the Remix IDE, and then create a new file name `ArcadeTokenSafeMath.sol`. Copy the contents of the starter file for this activity into the new `ArcadeTokenSafeMath.sol` file to help you get started.

2. Add the following `import` statement just after the `pragma` statement and before the contract definition:

    ```solidity
    import "github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";
    ```

3. Define a smart contract named `ArcadeToken`.

4. Add the following as the first line of code in your smart contract:

    ```solidity
    using SafeMath for uint;
    ```

    > **Note** This statement links the SafeMath library to the `uint` type. You can then call functions like `.add`, `.sub`, `.mul`, and `.div` directly from a `uint`, rather than using operators like plus (`+`), minus (`-`), times (`*`), and divided by (`/`).

5. Replace every math operation in the contract with its SafeMath equivalent. For example, the following code:

    ```solidity
    balances[msg.sender] -= value;
    ```

becomes:

    ```solidity
    balances[msg.sender] = balances[msg.sender].sub(value);
    ```

6. Deploy and test your contract. (You should now be safe from any integer underflows and overflows.)

    > **Hint** Remember to include the variable reassignments. SafeMath doesn’t change the variables that it operates on. You must reassign the variables with an equal sign (`=`)&mdash;for example, `balances[recipient] = balances[recipient].add(value);`.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

