# Hashing a Block

In this activity, you'll create a Streamlit application that can create a new block of data and display the hash for that block.

## Instructions

Open Visual Studio Code and use the [starter file](Unsolved/app.py) provided to complete the following steps:

1. Review the provided code in the `app.py` file for both the `Block` data class and the Streamlit web application. This mirrors what you created in a prior activity.

2. Inside the provided `Block` class, add a function named `hash_block`. This function should include an instance of the `sha256` hashing function, the processes to encode and hash the data, the creator ID, and the timestamp. The function should return the resulting hashes in a `hexdigest` format.

3. Inside the Streamlit “Add Block” button:

    * Add the code to call the `hash_block` function on the new block that gets created from entering data into the text area. Save the result of calling the function in a variable named `block_hash`.

    * Use the Streamlit `st.write` function to display the value of `block_hash` on the webpage.

4. Test the application. To do so, complete the following steps:

    * In the terminal, navigate to the `Unsolved` folder for this activity.

    * Be sure that your Conda development environment is active.

    * Run the Streamlit app in the terminal by using `streamlit run app.py`.

    * Add a new block of text data, and then review the resulting block hash.

---
© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
