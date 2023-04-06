# Automating Ethereum

In this activity, you will add functions that automate the process of accessing the balance from the Ganache local blockchain, as well as sending a signed transaction to the from one address to another. You will then incorporate these functions into the Streamlit web application.

## Instructions

This activity is broken down into two main sections:

 1. Create the `get_balance` function and add it to the Streamlit application.

 2. Create the `send_transaction` function and add it to the Streamlit application.

Complete the following steps:

Start by adding your mnemonic seed phrase to the `SAMPLE.env` file included in the activity's `Unsolved` folder. Once the variables have been added, resave this as a `.env` file.

### Part 1: Create the get_balance Function and Add It to the Streamlit Application

1. Open the `ethereum.py` file. Create a Python function called `get_balance`. The function will take one argument called `address`.

2. Call the `w3.eth.get_balance` function and pass it the `address` argument. Set this function call equal to a variable called `wei_balance`.

3. Call the `w3.fromWei` function and pass it `wei_balance` as an argument. Specify that you want to convert the wei balance to ether. Set this call equal to a variable called `ether`.

4. Return the `ether` balance from the function.

5. Open the `app.py` file, and then import the `get_balance` function from the `ethereum.py` file.

6. In the `Display Ethereum Account Balance` section, call the `get_balance` function and pass it the `account.address`. Set this function call equal to a variable called `ether_balance`.

7. Write the `ether_balance` to the Streamlit page.

8. Save your files. Navigate to the Unsolved folder inside a terminal instance. Run the application by typing `streamlit run app.py`.  Both your account address and ether balance should display to the Streamlit page.

### Part 2: Create the send_transaction Function and Add It to the Streamlit Application

1. Return to the `ethereum.py` file. Create a Python function called `send_transaction`. The function will take three arguments called `account`, `receiver`, and `ether`.

2. Inside the function, set a medium gas price strategy by calling the function `w3.eth.setGasPriceStrategy(medium_gas_price_strategy)`.

3. Call the `w3.teWei` function and pass it the argument `ether`. You will also need to specify that "ether" is the denomination of the value being converted. Finally, set this function call equal to the variable `wei_value`.

4. Estimate the gas it will take to mine the transaction. Call the function `w3.eth.estimateGas` and pass it three arguments as key:value pairs, as the following code shows:

    ```python
    { "to": receiver, "from": account.address, "value" : wei_value}
    ```

   This function should be set equal to the variable `gas_estimate`.

5. Construct the transaction object. Set the transaction object equal to the variable `raw_tx`. The keys you will need complete are: "to", "from", "value", "gas", "gasPrice" (the corresponding value is `w3.eth.generateGasPrice`) and the "nonce" (the corresponding value is `w3.eth.getTransactionCount(account.address)).

6. Call the `account.signTransaction` function and pass it the `raw_tx` as an argument. Set this equal to a variable called `signed_tx`.

7. Return the `w3.eth.sendRawTransaction` function. You will need to pass `signed_tx.rawTransaction` as the function argument.

8. Navigate back to the `app.py` file. Import the `send_transaction` function from the `ethereum.py` file.

9. In the `An Ethereum Transaction` section, create two user input fields:

    * A text input field that will take in the receiver's Ethereum address. Set this equal to a variable called `receiver`.

    * A number input field that will take in the amount of ether to be sent in the transaction. Set this equal to a variable called `ether`.

10. Create a Streamlit button that reads **Send Transaction**. Inside the button, call the `send_transaction` function and pass three arguments: `account`, `receiver` and `ether`. Set this function call equal to a variable called `transaction_hash`.

11. Create a Streamlit markdown line that reads "## Ethereum Transaction Hash:"

12. Write the `transaction_hash` to the page.

13. Save your files, and then test the application by completing the following steps:

    * Navigate to the `Unsolved` folder inside a terminal instance.

    * Run the application by typing `streamlit run app.py`. Both your account address and ether balance should display on the Streamlit page.

    * Add values to the `receiver` and `ether` input fields and click the **Send Transaction** button. Get the receiver address from your list of addresses in Ganache. The transaction hash should be displayed on screen.

14. Review the transaction in your Ganache application.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
