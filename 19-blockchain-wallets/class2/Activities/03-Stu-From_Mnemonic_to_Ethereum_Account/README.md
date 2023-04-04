# From Mnemonic to Ethereum Account

In this activity, you will use the mnemonic and BIP-44 packages and the Web3.py library to generate a wallet instance and a new, secure public-private key phrase from a mnemonic seed phrase.

## Background

You live in the United States, but you have family abroad in New Zealand. You would like to transfer funds internationally to your family in New Zealand. Because of the cost of doing this via the traditional banking system, you decide to send your family cryptocurrency funds over the Ethereum blockchain. Before you can create transactions to send your family funds on the Ethereum network, you must first generate a new digital signature in the form of an Ethereum public-private key pair.

## Instructions

Complete each of the following steps:

1. Import the following dependencies:

   * Import `os`.

   * From `dotenv`, import `load_dotenv` and call `load_dotenv`.

   * From `bip44`, import `Wallet`.

   * From `mnemonic`, import `Mnemonic`.

   * From `web3`, import `Account`.

2. Remember that you don't want to generate a new mnemonic every time you run the program, because you'll lose access to your previous mnemonic and subsequently your private key. If you have not already generated a mnemonic seed phrase and saved it to a `.env` file associated with this activity, you will need to generate one now.

   If you already have a mnemonic phrase that you would like to use for this activity, complete the following step:

      * Create a `.env` file in the same folder as the Jupyter notebook, and set the mnemonic phrase equal to an environment variable named `MNEMONIC`.

   If you do not already have a mnemonic seed phrase that you would like to use for this activity, create one by completing the following steps:

      * Call `os.getenv("MNEMONIC")`, and save its value as a variable named `mnemonic`.

      * Use an `if` statement to check if the mnemonic variable is `None`.

      * If the `mnemonic` variable is `None`, initialize a new `Mnemonic` instance and pass it a string value of “english” so that it will use the English word list. Save the instance as a variable named `mnemo`. Next, generate your mnemonic seed phrase by creating a variable named `mnemonic` and calling `mnemo.generate(strength=128)`. Finally, print out the mnemonic phrase.

      * Create a `.env` file in the same folder as the Jupyter notebook, and create an environment variable named `MNEMONIC`. Copy the new mnemonic seed phrase that you just generated and set it equal to the `MNEMONIC` variable.

3. Generate a `Wallet` instance using your `mnemonic` variable and the bip44 package.

   * Instantiate a new instance of the `Wallet` class from the bip44 package, and pass it your `mnemonic` variable to create a universal wallet instance. Save the wallet instance to a variable named `wallet`.

4. Derive public and private keys from your `wallet` instance. To do so, complete the following steps:

   * Create two variables, `public` and `private`, and set their values by calling the `derive_account` method on your wallet instance. In order to associate the account with Ethereum, pass the string “eth” to the `derive_account` method.

   * Create a new variable named `account`, and construct the Ethereum account by calling `Account.privateKeyToAccount` and passing it your private key variable.

   * Call `account.address` to access the address associated with your new Ethereum account. By using this address, other participants can send you ether on the Ethereum blockchain.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
