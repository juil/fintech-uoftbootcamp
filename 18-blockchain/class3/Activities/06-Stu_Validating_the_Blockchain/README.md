# Validating the Blockchain

In this activity, you will use Streamlit to test the validation functionality associated with the PyChain.

## Instructions

Review the code included in the [`app.py` file](Unsolved/app.py), and then complete the following steps:

1. Write the code that validates the integrity of the PyChain by comparing the calculated hash code of each block to the `prev_hash` value contained in the following block.

2. Add a button with the text “Validate Blockchain” to your Streamlit interface.

3. Code the Validate Blockchain button so that when it’s clicked, it calls the `is_valid` method of the `PyChain` data class and then writes the result to the webpage.

4. Test the application. To do so, complete the following steps:

    * In the terminal, navigate to the `Unsolved` folder for this activity.

    * Be sure that your Conda development environment is active.

    * Run the Streamlit app from the terminal by using `streamlit run app.py`.

    * Type some input text in the text box, and then click the “Add Block” button. This adds a block to the chain. Repeat this step.

    * Click the Validate Blockchain button to validate the current ledger.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
