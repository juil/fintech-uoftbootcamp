# Transactions with Web3.py

In this activity, you will create your own transaction between Ethereum accounts. You will use Web3.py to connect to a local mock development blockchain. Then, you will create, send, and review a financial transaction by using several Web3.py methods.

## Instructions

Complete each of the following steps:

1. From the Web3.py library, import `Web3` and the `EthereumTesterProvider`.

2. Define a variable named `w3`, and set it equal to a new `Web3` instance.

3. Define a variable named `provider`, set it equal to `EthereumTesterProvider`, and then pass it to the `Web3` instance.

4. Call `w3.eth.accounts` and print the result. Next, define two new string variables named `sender` and `receiver`. Copy two of the account addresses from the list of accounts. Set one account address as the string for the `sender` variable, and set the other account address as the string for the `receiver` variable.

5. Set the units of `gas` to 21,000 to ensure that your transaction will be mined and added to the blockchain.

6. Use the `w3.toWei` function to convert 333 ether into the equivalent denomination of wei. Save the amount in wei as a variable named `value`.

7. Call `w3.eth.send_transaction` and pass it `receiver` as the `to` parameter, `sender` as the `from` parameter, `gas` as the `gas` parameter, and the `value` variable as the `value` parameter.

8. Call the [`eth.getTransactionReceipt`](https://web3js.readthedocs.io/en/v1.2.0/web3-eth.html#gettransaction) function and pass the hash code that is returned from sending the transaction as the parameter to review the transaction receipt.

9. Call the `eth.get_block` function and pass it the parameter `latest`. Confirm that you can see the HexBytes code from your transaction in the information provided.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
