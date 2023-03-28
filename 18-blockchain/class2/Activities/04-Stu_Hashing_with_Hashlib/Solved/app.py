# Hashing With Hashlib
################################################################################
# In this activity, you’ll use the hashlib library and Streamlit to build an
# application that can hash any text input.

# Complete the following steps:
# 1. Create a function to hash an input value.
# 2. Add a streamlit `text_area` component to accept text from the user.
# 3. Add a streamlit button called "Hash Text". When the button is clicked,
# use the hash_text function to generate a hash of the user's text and
# display the resulting hash to the page.
# 4. Test the application.
################################################################################
# Imports
import hashlib
import streamlit as st

################################################################################
# Step 1:
# Create a function to hash an input value.
#
# To do so, define a function named
# `hash_data` that accepts user input, encodes that input, and returns a hash
# of the data.

# Hint: Inside the `hash_data` function, use the`sha256` function from hashlib
#  to generate the hash of the data.

# Define a function called `hash_data` that takes in a parameter called `data`
def hash_data(data):

    # Instantiate an instance of hashlib's `sha256` function
    sha = hashlib.sha256()

    # Use the `encode` function to encode the string version of the data that
    # was passed in as a parameter to the function
    encoded_data = str(data).encode()

    # Call the hashing instance and the `update` function. Pass it the encoded
    # data as a parameter
    sha.update(encoded_data)

    # Return the unique hash of the data using the `hexdigest` function
    return sha.hexdigest()

################################################################################
# Streamlit Code


# Create the application header using a markdown string
st.markdown("# Create a Unique Hash of Data")

################################################################################
# Step 2:
# Add a Streamlit `text_area` component to accept data from the user. Use the 
# Streamlit write function to display the length of the input data back to the user.

# Add a Streamlit `text_area` component to accept data from the user
# Be sure to convert the input data to a string
# Use the `encode` function to encode the input data
input_data = str(st.text_area("Enter Data")).encode()

# Use the Streamlit `write` function to display the length (`len`) of the input
# data back to the user
st.write(f"Input Length: {len(input_data)}")

################################################################################
# Step 3:
# Add a Streamlit `button` named “Hash Text”. When the button is clicked, use
# the `hash_data` function to first generate a hash of the user's text and then
# display that hash on the page.

# Add a Streamlit `button` named “Hash Text”
if st.button("Hash Text"):

    # Generate a hash of the user input using the `hash_data` function
    input_hash = hash_data(input_data)

    # Use the Streamlit `write` function to display the unique hash of the data
    st.write(f"Output Hash (fingerprint): {input_hash}")

    # Use the Streamlit `write` function to display the length of the output hash.
    st.write(f"Output Length: {len(input_hash)}")
################################################################################
# Step 4:
# Test the application.

# Complete the following steps:
# 1. In the terminal, navigate to the `Unsolved` folder for this activity.
# 2. Be sure that your Conda development environment is active.
# 3. Run the Streamlit app in the terminal by using `streamlit run app.py`.
# 4. Navigate to [Lorem Ipsum](https://www.lipsum.com/), generate some lorem ipsum, and then paste the generated text.
# 5. Hash the encoded data by clicking the Hash Text button. Make a note of the unique fingerprint for the data.
# 6. Change one word of the input text in the text box. Then hash the text again to find out how the hash changes as the input changes.

################################################################################
