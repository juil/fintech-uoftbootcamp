# Ethereum Through Web3.py

In this activity, you’ll take your new Web3.py skills for a test drive and fetch accounts and balances from your own mock development blockchain instance.

## Background

You are a software developer at a large international bank that hopes to leverage the Ethereum network to send international transactions quickly and with low fees. Apply your knowledge of Web3.py to create a basic Python program for interacting with the Ethereum blockchain.

## Instructions

Complete each of the following steps:

1. From the Web3.py library, import `Web3` and the `EthereumTesterProvider`.

2. Define a new variable named `w3`, and set it equal to a new `Web3` instance.

3. Define a variable named `provider`. Set this variable equal to `EthereumTesterProvider`, and then pass it to the `Web3` instance.

4. Call `w3.eth.get_block('latest')`, and print the result to check that your mock blockchain is working.

5. Call `w3.eth.accounts`, and print the result to view your available accounts on the blockchain.

6. Call `w3.eth.get_balance` and pass it to one of your available addresses as a string to check the balance of the account on the chain. Save the balance as a variable named `wei_balance`.

7. Use the `w3.fromWei` function to convert your balance from wei to ether.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
