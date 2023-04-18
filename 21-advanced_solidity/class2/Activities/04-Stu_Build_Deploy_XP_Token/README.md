# Build and Deploy XP_Token

## Instructions

Note that the starter code contains the basic `XP_Token` contract structure and imports of the `ERC20` and `ERC20Detailed` contracts that implement the ERC-20 standards.

### Make Your Contract Operational

1. Starting with the `onlyOwner` modifier, add a `require` statement that checks if `msg.sender` is equal to the `owner` of the contract.

    * Leave the underscore and semicolon (`_;`) at the end of the function. This way, the Solidity program will return to the function that called the modifier.

2. For the definition of the constructor function, pass it the variables that `ERC20Detailed` expects: `string name`, `string symbol`, and `uint decimals`. Use the following values:

      * "XP_Token" for the first parameter.

      * "XPT" for the second parameter.

      * 18 for the third parameter. (This sets the `decimals` parameter of your token to be the same as that of Ethereum ether.)

3. Within the constructor, set `owner` to `msg.sender`. Then call the internal `_mint` function, and give the `initial_supply` to the `owner`.

4. In the `mint` function, call the internal `_mint` function in the same way, except pass the `recipient` and `amount` parameters to `_mint` instead.

5. Restrict the `mint` function so that only the owner can call it. To do so, add `onlyOwner` to the function's modifiers. Specifically, add `onlyOwner` after the `public` modifier.

### Compile, Deploy, and Test Your Contract

1. Close and relaunch Ganache on your local machine.

2. Open the MetaMask browser extension in Google Chrome, and then import at least two accounts from the updated list of Ganache test accounts. You need the private key information from Ganache to import each account. Confirm that the addresses now listed in MetaMask match the addresses that are associated with the accounts in Ganache.

3. Navigate back to the Remix IDE, and then compile your completed `XP_Token` contract.

4. When the contract finishes compiling, navigate to the **Deploy & Run Transactions** page, and then choose the **Injected Web3** environment to deploy the contract. When the MetaMask window opens, you need to select the accounts from MetaMask that you want to use for the `XP_Token` contract deployment.

    > Hint: Make sure to select the accounts that you imported most recently. Remember that Ganache updates the account information every time it relaunches.

5. Deploy the `XP_Token` contract by creating an initial supply of tokens and then clicking the **transact** button. When the MetaMask window opens, confirm the transaction. Be sure to note the gas fee that’s required to deploy the contract.

6. Confirm that the balance of tokens associated with the owner account matches that of your initial supply.

7. Navigate to Ganache, select the **Transactions** tab, review the address that’s associated with the deployed contract, and then copy that address. Confirm that the address matches that of the deployed contract in the Remix IDE.

8. Reload the Remix IDE webpage. This deletes the original contract deployment from the Remix page. Navigate back to the **Deploy & Run Transactions** page, paste the deployed contract address into the **Load contract from Address** box, and then click **AtAddress**.

9. Confirm that the number of tokens in the balance of the owner account matches that of the initial deployment.

10. Note that you’ve successfully written, deployed, and tested a token that’s ERC-20 compliant! Congratulations!

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

