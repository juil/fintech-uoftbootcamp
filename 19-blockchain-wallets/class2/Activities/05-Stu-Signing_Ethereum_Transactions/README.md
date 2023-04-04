# Signing Ethereum Transactions

In this activity, you will use the Web3.py library to sign and authorize messages using your public-private key pair.

## Background

You are a treasury agent working for the United States Department of the Treasury to create a new internal audit system for federal financial documents. In this new system, each member of your agency has a copy of every employee's public key. The public keys are used to verify who has published or edited a given financial document. Your task is to test this system by creating, signing, and verifying a message using your public-private key pair.

## Instructions

Complete each of the following steps:

1. In the `Unsolved` folder, add the `.env` file that contains the mnemonic seed phrase that you generated in the first activity. Be sure to save this as the variable `MNEMONIC`.

2. Call `os.getenv("MNEMONIC")` and save its value as a variable named `mnemonic`. Confirm that your seed phrase is available by checking the `type` of your `mnemonic` variable.

    **Hint:** The information contained in a `.env` file should never be displayed to a program’s user. To confirm that the information is available, you can check the data type of the variable using the syntax `type(variable)`. If the variable has been imported correctly, the result should be a data type “str”, indicating that it is a string variable.

3. From the BIP-44 package, generate a `wallet` instance and pass your `mnemonic` variable as the parameter.

4. Derive public and private keys from your `wallet` instance; save the values as two variables, `public` and `private`.

    **Hint:** Remember that with the code we’re using today, generating a wallet with the same mnemonic seed phrase will generate the same private key and account information every time we run the program.

5. Using the `Account` object and the `privateKeyToAccount` function, use your private key to generate an Ethereum account. To confirm that the account was successfully initiated, print the account’s address.

6. Create a new string variable named `msg`, and set its value equal to any message you would like to sign&mdash;e.g., “Zach owes Glenna $40.”

7. Use `encode_defunct(text=msg)` from Web3.py to byte encode your message. Save the output as a variable named `encoded_msg`.

8. Call the `w3.eth.account.sign_message` method. Pass it your encoded message variable and your private key. Your private key will “sign” your new message. Save the returned signed message as a variable named `signed_message`.

9. Call the `w3.eth.account.recover_message` method. Pass it your encoded message variable and the message’s signature from the `signed_message.signature`. Confirm that the returned value matches the account address that was printed in Step 5.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
