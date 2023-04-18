# XP Token

In this activity, you’ll use your knowledge of Solidity to build an `XP_Token` smart contract.

You’ll also use the OpenZeppelin SafeMath library to secure the smart contract from integer underflow errors.

The `XP_Token` contract will allow you to collect ether in exchange for XP Tokens (XPT) that users can spend at a company website that accepts only XPT tokens.

## Instructions

1. Open the Remix IDE, and then create a new contract named `XP_Token.sol`.

2. Set the `pragma` to any version from 0.5.0 to 0.5.17.

3. Add the following `import` statement just after the `pragma` statement and before the `contract XP_Token` definition:

    ```solidity
    import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";
    ```

4. After you define and name your `XP_Token` contract, add the following as the first line of code in your smart contract:

    ```solidity
    using SafeMath for uint;
    ```

5. Add the following contract variables:

    * A `address payable` variable named `owner`. Set this variable to `msg.sender`. Since this is only called once during the deployment, you will become the contract owner.

    * A `string` variable named `symbol`. Set this variable to `XPT`. Make sure that you set this variable to `public`&mdash;so that wallets like MetaMask will recognize the ticker of your token.

    * A `uint public` variable named `exchange_rate`. Set this variable to the number of tokens that you want to distribute per wei.

6. Add a mapping named `balances` that maps `address` values to `uint` values.

7. Add a `public view` function named `balance` that returns a `uint` as follows:

    * This function should return the balance of `msg.sender` by accessing the `balances` mapping and using `msg.sender` as the key.

8. Add a `transfer` function that accepts `address recipient` and `uint value` as parameters. Within this function, complete the following steps:

    * Using the SafeMath library, subtract `value` from the balance of `msg.sender` in the `balances` mapping.

    * Using the SafeMath library, add `value` to the balance of `recipient` in the mapping.

9. Add a way for customers to purchase new XPT tokens. To do so, add a `public payable` function named `purchase`. It doesn’t need any parameters. Within the function, complete the following steps:

    * Using the SafeMath library, calculate a new `uint` named `amount` by multiplying `msg.value` by `exchange_rate`. (This calculates the number of tokens to distribute.)

    * Using the SafeMath library, add `amount` to the balance of `msg.sender`.

    * Transfer `msg.value` to the `owner` address.

10. Add a way for you, as the business owner, to create new tokens. To do so, add a new function named `mint` by completing the following steps:

    * Use the same parameters as you did for the `transfer` function that you defined earlier.

    * At the beginning of the function, require that `msg.sender` be equal to `owner`. Make sure to include an error message in the `require` statement.

    * Using the SafeMath library, Add `value` (the number of minted tokens) to the balance of the recipient address in the mapping.

11. Test your contract by deploying it and then calling the functions that the Remix IDE exposes. Try minting some tokens by using a Remix address and then sending them to another Remix address. Confirm that you don’t get an integer underflow error.

    > **Hint** Remember that a mapping associates one data type with another. By pairing `address` with `uint`, you can track account balances.
    >
    > For example, a mapping might store data that resembles the following:
    >
    > `0xc3879B456DAA348a16B6524CBC558d2CC984722c => 333`.
    >
    > For more details about how mappings work, visit [Mapping Types](https://solidity.readthedocs.io/en/v0.5.13/types.html#mapping-types) in the Solidity documentation.

12. Celebrate the fact that you can now build what most people perceive as magical tokens! You can also extend these contracts to do anything that you'd like. You can create a complex system of value that’s customizable to any use case.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.