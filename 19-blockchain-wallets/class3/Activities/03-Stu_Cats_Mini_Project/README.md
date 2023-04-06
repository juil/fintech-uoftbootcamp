# Cats Mini Project

## Background

You are a developer working for a large e-commerce and gaming platform that wants to expand its customer base and begin selling virtual cats online. They have tasked you&mdash;a skilled blockchain developer&mdash;with building the first prototype; it should have a user interface and be able to check account balances before allowing transactions to be sent.

## Instructions

Complete each of the following steps:

1. In the `Unsolved` folder, create your `.env` file, which should contain your mnemonic seed phrase saved as the variable `MNEMONIC`.

2. Navigate to the Ganache, log in to your application, and copy your mnemonic seed phrase.  Save the project id in your `.env` file as a variable named `MNEMONIC`.

3. Inside the `generate_account` function, use the mnemonic seed phrase you created in the previous lesson and the `Wallet()` class from the bip44 package to generate a wallet instance. Then, derive your private and public keys by calling the `.derive_account` method on the `wallet` object and passing it the string “eth”. Save the two returned values as variables named `private` and `public`.

4. Pass the private-key value to `Account.privateKeyToAccount`, and save the returned `account` object as a variable named `account`.

5. Call `account.address` and save it as a new variable named `account_address`. Then, print the `account_address` variable to get your public Ethereum address from your public key.

6. In the Jupyter notebook, fetch the balance of your Ethereum address by using Web3.py. To do so, complete the following steps:

    * Then begin building the `get_balance` function.

    * Call the `w3.eth.getBalance` method, and pass it the `account_address` variable. Save the returned value as a variable named `wei_balance`.

    * Call the function `w3.fromWei`, and pass it your `wei_balance` variable and the string “ether”. Save the returned value as a variable named `ether`. Print your account balance in ether.

7. Navigate to the `cat_shop.py` file.

8. Import the following functions from the `crypto_wallet.py` file:

     * `generate_account`

     * `get_balance`

9. Review the provided code, which you will be adding to in the next step.

10. In the `for` loop inside the `get_cats` function, use `st.write` to add the objects from the object above into the code that provides the cat’s information, such as the price and name.

11. Then, create Streamlit application headings using `st.markdown` to explain that this app is for buying cats.

12. Call the `generate_account` function, and save it as a variable called `account`.

13. Call the `get_balance` function, and save it as a variable `ether`.

14. Create a select box to choose a cat using `st.sidebar.selectbox`.

15. Create a header using `st.sidebar.markdown()` to display cat name and price.

16. Create a variable called `cat_price` to retrieve the cat price from the `cat_database` using block notation.

17. Use a conditional statement with the `if` keyword to check if the selected cat can be purchased. This statement will check if the `ether` variable that we created&mdash;that is, the account balance&mdash;is greater than or equal to the `cat_price`.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
