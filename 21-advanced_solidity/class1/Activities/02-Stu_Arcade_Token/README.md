# Arcade Token

In this activity, you’ll use the mapping data structure to build a token smart contract for use by an arcade&mdash;or by any other business that you’d like!

This contract will allow you, as the business owner, to collect ether in exchange for tokens that users can spend at your business.

## Instructions

1. Open the Remix IDE, and then create a new file named `XP_Token.sol`.

    > **Note** To help you get started, you can copy the contents of the starter file for this activity into the new `XP_Token.sol` file.

2. Set the `pragma` to any version from 0.5.0 to 0.5.17.

3. Define a contract, and either name it `ArcadeToken` or choose another name that’s appropriate for your business.

4. Add the following variables to your contract:

    * An `address payable` variable named `owner`. Set this variable to `msg.sender`. (This will set you as the contract owner when the contract gets deployed.)

    * A `string` variable named `symbol`. Set this variable to the string “ARCD” or another appropriate ticker. Make sure that you set this variable to `public`&mdash;so that other blockchain participants can recognize the ticker for your token.

    * A `uint public` variable named `exchange_rate`. Set this variable to the number of tokens that you want to distribute per wei.

    * A mapping named `balances` that maps `address` values to `uint` values.

5. Add a new `public view` function named `balance` that returns a `uint` as follows:

    * This function should return the balance of `msg.sender` by accessing the `balances` mapping and using `msg.sender` as the key.

6. Add a new function named `transfer` that accepts `address recipient` and `uint value` as parameters. Within this function, complete the following steps:

    * Subtract `value` from the balance of `msg.sender` in the `balances` mapping.

    * Add `value` to the balance of `recipient` in the mapping.

6. Add a way for customers to purchase new tokens. To do so, add a `public payable` function named `purchase`. It doesn’t need any parameters. Within the function, complete the following steps:

    * Calculate a new `uint` named `amount` by multiplying `msg.value` by `exchange_rate`. (This calculates the number of tokens to distribute.)

    * Add `amount` to the balance of `msg.sender`.

    * Transfer `msg.value` to the `owner` address.

7. Add a way for you, as the business owner, to create new tokens. To do so, add a new function named `mint` by completing the following steps:

    * Use the same parameters as you did for the `transfer` function that you defined earlier.

    * At the beginning of the function, require that `msg.sender` be equal to `owner`. Make sure to include an error message in the `require` statement.

    * Add `value` (the number of minted tokens) to the balance of the recipient address in the mapping.

8. Test your contract by deploying it and then calling the functions that the Remix IDE exposes. Try minting some tokens for yourself and then sending them to another address.

    > **Hint** Remember that a mapping associates one data type with another. By pairing `address` with `uint`, you can track account balances.
    >
    > For example, a mapping might store data that resembles the following:
    >
    > `0xc3879B456DAA348a16B6524CBC558d2CC984722c => 333`.
    >
    > For more details about how mappings work, visit [Mapping Types](https://solidity.readthedocs.io/en/v0.5.13/types.html#mapping-types) in the Solidity documentation.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

