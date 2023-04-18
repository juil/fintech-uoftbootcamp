/*
XP_Token

Instructions

Complete the following steps:

1. Open up the Remix IDE, and create a new contract called `XP_Token.sol`.

2. Set the `pragma` to any version from 0.5.0 to 0.5.17.

3. Add the following import statement just below the `pragma` and above the `contract XP_Token` definition:

  ```solidity
  import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";
  ```

4. After you define and name your contract `XP_Token`, add the following as the first line of code in your smart contract:

  ```solidity
  using SafeMath for uint;
  ```

5. Next, add the following contract variables:

    * A `address payable` called `owner`. Set this to `msg.sender`. Since this is only called once during the deployment, you will become the contract owner.

    * A `string` called `symbol`. Set this to `XPT` and make sure that it is `public`. Setting the symbol will allow wallets like MetaMask to recognize your token's symbol/ticker.

    * Set an `exchange_rate` variable to equal the number of tokens to be distributed per `wei`. Make sure the variable is a `uint public` type!

6. Add the data structure `mapping`:

    * Create a new `mapping` that pairs `address` to `uint`. Name this variable `balances`.

7. Add a new function called `balance` that is a `public view` that `returns(uint)`:

    * This function should return the `balances` of `msg.sender` by accessing the `balances` mapping, using `msg.sender` as the index/selector/key.

8. Add a new `transfer` function that accepts `address recipient` and `uint value` as parameters:

    * Using the SafeMath library, this function, subtract `value` from the balance of `msg.sender` in the `balances` mapping.

    * Again using the SafeMath library, add the `value` to the `recipient` balance in the mapping.

9. Users will now need a way to purchase new `XPT` tokens! Add a `public payable` function called `purchase`. It does not need any parameters. Within the function:

    * Using the SafeMath library, calculate a new `uint` called `amount` by multiplying `msg.value` with the `exchange_rate`. This equation will calculate the number of tokens to distribute.

    * Again using the SafeMath library, add the `amount` to the balance of `msg.sender`.

    * At the end of the function, transfer the `msg.value` to the `owner` address. (Remember, `owner` must be set to `payable` to call `.transfer` on it)

10. Finally, since you as the company owner will need to create new tokens when you need to, add a new function called `mint`:

    * Use the same parameters as the `transfer` function you defined earlier.

    * At the beginning of the function, `require` that the `msg.sender` is equal to `owner`. Make sure to put an error message in the `require`.

    * Using the SafeMath library, add the `value` you'd like to the `recipient` address' balance in the mapping.

11. Test out your contract by deploying and calling the functions that Remix exposes. Try minting some tokens using a Remix address, then sending some to another Remix address. Be sure to confirm that you do not have an integer underflow error!

*/

pragma solidity ^0.5.0;

// @TODO: import the SafeMath library via Github URL
// YOUR CODE HERE!

contract XP_Token {
    // @TODO: add the "using SafeMath..." line here to link the library to all uint types
    // YOUR CODE HERE!

    // @TODO: add the three contract variables: owner, symbol, and exchange_rate
    // YOUR CODE HERE!
    // YOUR CODE HERE!
    // YOUR CODE HERE!

    // @TODO: add the data structure mapping for the user balances
    // YOUR CODE HERE!

    // @TODO: Add a new function called `balance`
    // YOUR CODE HERE!

    // @TODO: Add a new function called `transfer`. Use the SafeMath library.
    // YOUR CODE HERE!

    // @TODO: Add a new function called `purchase`. Use the SafeMath library.
    // YOUR CODE HERE!

    // @TODO: Add a new function called `mint`. Use the SafeMath library.
    // YOUR CODE HERE!
    }
}
