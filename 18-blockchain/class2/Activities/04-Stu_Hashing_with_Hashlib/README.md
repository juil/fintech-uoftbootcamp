# Hashing with Hashlib

In this activity, you will use the hashlib library and Streamlit to build an application that can hash any text input.

## Instructions

Use Visual Studio Code and the [starter file](Unsolved/app.py) provided to complete the following steps:

1. Create a function to hash an input value. To do so, define a function named `hash_data` that accepts user input, encodes that input, and returns a hash of the data.

    > **Hint** Inside the `hash_data` function, use the`sha256` function from hashlib to generate the hash of the data.

2. Add a Streamlit [text_area](https://docs.streamlit.io/en/stable/api.html?highlight=text_area#streamlit.text_area) component to accept input data from a user. Use the Streamlit [write](https://docs.streamlit.io/en/stable/api.html?highlight=write#streamlit.write) function to display the length of the input data back to the user.

3. Add a Streamlit [button](https://docs.streamlit.io/en/stable/api.html?highlight=button#streamlit.button) named “Hash Text”. When the button is clicked, use the `hash_data` function to first generate a hash of the user's data and then display that hash on the page.

4. Test the application. To do so, complete the following steps:

    * In the terminal, navigate to the `Unsolved` folder for this activity.

    * Be sure that your Conda development environment is active.

    * Run the Streamlit app in the terminal by using `streamlit run app.py`.

    * Navigate to [Lorem Ipsum](https://www.lipsum.com/), generate some lorem ipsum, and then paste the generated text.

    * Hash the encoded data by clicking the Hash Text button. Make a note of the unique fingerprint for the data.

    * Change one word of the input text in the text box. Then hash the text again to find out how the hash changes as the input changes.

---
© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
