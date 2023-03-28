# Blockchain Application

In this activity, you will enhance a Streamlit application that can both generate new blocks of user data and add them to a Python blockchain.

## Instructions

Use Visual Studio Code and the [starter file](Unsolved/app.py) provided to complete the following steps:

1. Review the provided code in the `app.py` file for both the `Block` data class and the Streamlit web application. This mirrors what you created in a prior activity.

2. In `app.py`, modify the Streamlit “Add Block” button code so that when someone clicks the button, the code adds a new block to the blockchain. Make sure to include the following steps:

    * Select the previous block in the chain by using the following code:

      `prev_block = pychain.chain[-1]`.

    * Hash the previous block by using the following code:

      `prev_block_hash = prev_block.hash_block()`.

    * Create a new block by using the following code:

      `new_block = Block(data=input_data, creator_id=42, prev_hash=prev_block_hash)`.

    * Add the new block to the chain by using the following code:

      `pychain.add_block(new_block)`.

3. To display the `PyChain` ledger data on the Streamlit webpage, complete the following steps in `app.py`:

    * Create a Pandas DataFrame so that the block data will display in a more user-friendly manner. To do so, use the following code:

      `pychain_df = pd.DataFrame(pychain.chain)`.

    * Write the Pandas DataFrame to the screen by using the `st.write` function.

4. Test the application. To do so, complete the following steps:

    * In the terminal, navigate to the `Unsolved` folder for this activity.

    * Be sure that your Conda development environment is active.

    * Run the Streamlit app in the terminal by using `streamlit run app.py`.

    * Adjust the input text in the text box, and then click the “Add Block” button.

    * Review the changes in the `PyChain` ledger that the Streamlit application webpage reflects.

---
© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
