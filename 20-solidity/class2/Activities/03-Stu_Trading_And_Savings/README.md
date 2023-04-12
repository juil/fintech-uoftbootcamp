# Trading and Savings Contracts

## Background

You work for a corporate banking firm that’s planning to offer investment options in cryptocurrencies to its customers. As a fintech professional with experience in Solidity programming, you’ve been asked by your manager to create two smart contract prototypes: one that keeps track of trading transactions and another that helps customers manage their personal savings.

## Instructions

Open the [Remix IDE](http://remix.ethereum.org/), import the provided starter file, and then complete the following steps:

1. Use the `latest_trade.sol` file to create a contract named `LatestTrade` that contains the following:

    * A string variable named `coin` that has the value `XRP` assigned to it.

    * An unsigned integer variable named `price`.

    * A Boolean variable named `is_buy_order`.

2. Add a function named `updateTrade` to the `LatestTrade` contract as follows:

    * Define an in-memory string variable named `new_coin` as the first parameter.

    * Define an unsigned integer variable named `new_price` as the second parameter.

    * Define a Boolean variable named `is_buy` as the third parameter.

    * In the body of the function, set the `coin`, `price`, and `is_buy_order` contract variables as the inputs to the `updateTrade` function. This function will update the contract variables via the `updateTrade` function.

3. Add a public getter function named `getTrade` to the `LatestTrade` contract as follows:

    * The `getTrade` function returns the `coin`, `price`, and `is_buy_order` variables of the `LatestTrade` contract.

4. Modify the `personal_savings.sol` starter file as follows:

    * Define a public function named `withdraw` that has two input parameters: an unsigned integer named `amount` and a payable address named `recipient`.

    * In the body of the `withdraw` function, set the return value to the result of the `transfer` function on the `recipient` address. Note that the `transfer` function uses the `amount` parameter to get this result.

    * Add a public payable function named `deposit`.

    * Add a payable fallback function.

5. Compile the file to ensure that the code works.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.