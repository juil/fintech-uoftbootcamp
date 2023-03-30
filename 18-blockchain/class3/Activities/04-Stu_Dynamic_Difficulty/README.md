# Dynamic Difficulty

In this activity, you will use Streamlit to test the integration of the proof of work consensus mechanism in your PyChain application.

## Instructions

Review the code included in the [`app.py` file](Unsolved/app.py), and then complete the following steps:

1. Add a `difficulty` data attribute to the `PyChain` data class. Use a data type of `int` and a default value of 4.

2. In the `proof_of_work` method of the `PyChain` data class, add a `num_of_zeros` data attribute that multiplies the string value ("0") by the `difficulty` value.

3. Add a Streamlit component that can update the `difficulty` attribute of the `PyChain` class. To do so, complete the following steps:

    * Add a [Streamlit slider](https://docs.streamlit.io/en/stable/api.html?highlight=slider#streamlit.slider) component that allows the user to select a difficulty value from 1 to 5. Set the starting value to 4. Set this component equal to a variable named `difficulty`.

    * Although you can place your Streamlit slider anywhere on the page, consider placing it in a [Streamlit sidebar (`st.sidebar`)](https://docs.streamlit.io/en/stable/api.html?highlight=sidebar#add-widgets-to-sidebar).

    * Update the `difficulty` data attribute of the `PyChain` data class (`pychain.difficulty`) with this new `difficulty` value.

4. Test the application. To do so, complete the following steps:

    * In the terminal, navigate to the location in which your `app.py` file resides.

    * Be sure that your Conda development environment is active.

    * Run the Streamlit app from the terminal by using `streamlit run app.py`.

    * Create a new block in the Streamlit interface and confirm that it is added to the PyChain.

    * Change the difficulty, and then add another block. Observe how the change in difficulty level affects the overall time it takes to add a block to the chain with proof of work enabled.

---
© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
