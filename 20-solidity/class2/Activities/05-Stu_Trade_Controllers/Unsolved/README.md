# Trade Controllers

In this activity, you’ll gain practical experience with using conditional statements in Solidity. You’ll use basic logical operators and a control flow to build a smart contract that tracks trades in the Ethereum blockchain.

## Files

For this activity, you need to create a new Solidity file named `trade_controller.sol`.

## Instructions

1. Create a basic smart contract, named `TradeController`, as follows:

    ```Solidity
    pragma solidity ^0.5.0;

    contract TradeController {
    // insert code here
    }
    ```

2. Define two variables: a `uint` variable named `previousPrice` and a `string` variable named `tradeType`.

    > **Note** You use a `uint` variable to contain the previous price. This is because the price will always be a positive value. You’ll never have a negative price. You use `string` for the `tradeType` variable because its value can be “Buy”, “Sell”, or “Hold”.

3. Create a `public` function named `makeTrade`. This function should take a `uint` argument named `currentPrice` that represents the current price of the asset.

4. In the body of the `makeTrade` function, define a conditional statement that checks if the current price is less than the previous price. If this condition is true, set the `tradeType` variable to “Buy” and the previous price equal to the current price.

    > **Hint** Just like in Python, an `if` statement in Solidity consists of the `if` keyword followed by a condition that evaluates to true or false. Unlike in Python, parentheses surround the condition in Solidity.

5. Add a new `bool` argument to the `makeTrade` function, and name it `buyAnyway`.

6. Place `|| buyAnyway` at the end of the condition. This will allow the function to return `true` even if the current trade price is greater than the previous price. You might want to buy anyway, regardless of the previous price! Here’s the condition:

    ```solidity
    if (currentPrice < previousPrice || buyAnyway)
    ```

    > **Hint** The symbol consisting of two vertical bars ( `||` ) represents the logical OR operator. Python defines most logical operators with keywords in plain English, like `and`, `or`, and `not`. But, Solidity uses symbols. Two ampersands ( `&&` ) means AND, two vertical bars ( `II` ) means OR, and an exclamation point ( `!` ) means NOT. You can learn more about the logical operators in the [Booleans](https://docs.soliditylang.org/en/v0.5.0/types.html#booleans) section of the Solidity documentation.
    >
    > In plain English, this `if` statement now says the following: if the `currentPrice` value is less than the `previousPrice` value, or if `buyAnyway` is set to `true`, then continue.

7. Add an `else if` statement with a condition that checks if `currentPrice` is less than `previousPrice` so that we know when to sell.

8. For the case when the first two conditions evaluate to `false`, add a final `else` statement. In this statement, set `tradeType` to “Hold”, because you don’t want to buy or sell in this scenario.

9. Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.
