# Building a Blockchain Block
################################################################################
# In this activity, you’ll build a Streamlit application that accepts user
# input and then stores that input in a `Block` data class.

# The instructions for this activity are divided into the following high-level
# steps:
# 1. Create a data class for storing data from a user.
# 2. Create a Streamlit component to accept user input.
# 3. Create a button for storing and displaying the user input.
# 4. Test the application.

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import Any

################################################################################
# Step 1:
# Create a Data Class for Storing Data from a User

# In this section, you’ll create a data class named `Block` for storing data
# from a user. To do so, complete the following steps:
# 1. Define a class named `Block` and add the `@dataclass` decorator.
# 2. Inside the data class, define an attribute named `data` with a type of
# `Any`.
# 3. Inside the data class, define an attribute named `creator_id` with a type
# of `int`.
# 4. Inside the data class, define an attribute name `timestamp` with a type of
# `str`.
# 5. Assign a default value to the `timestamp` attribute by using the following
# code: `datetime.utcnow().strftime("%H:%M:%S")`

# Define a class `Block` and add the `@dataclass` decorator.
@dataclass
class Block:
    # Define an attribute named `data` with a type of `Any`.
    data: Any
    # Define an attribute named `creator_id` with a type of `int`.
    creator_id: int
    # Define an attribute name `timestamp` with a type of `str`.
    # Use the following code to set the value:
    # `datetime.utcnow().strftime("%H:%M:%S")`
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")


# Create the application headers using markdown strings.
st.markdown("# PyBlock")
st.markdown("## Store Data in a Block")

################################################################################
# Step 2:
# Create a Streamlit Component to Accept User Input

# Referencing the Streamlit library, use the `text_input` function and pass the
# parameter "Block Data".
input_data = st.text_input("Block Data")

################################################################################
# Step 3:
# Create a Button for Storing and Displaying the User Input

# In this section, you’ll create a button that will store the user input in an
# instance of the `Block` data class and then display it to the user. To do so,
# complete the following steps:
# 1. Create a Streamlit `button`, and pass the “Add Block” parameter to it.
# 2. In the button statement, create an instance of the `Block` data class. Use
# the user input from the preceding “Step 2” section for the data attribute,
# and use the integer 42 for the creator ID.
# Hint: Create an instance of the Block dataclass using the following code:
# `new_block = Block(data=input_data, creator_id=42)`
# 3. Use the `st.write` function to display the new block.

# Create a Streamlit `button`, and pass the “Add Block” parameter to it.
if st.button("Add Block"):
    # Create an instance of the `Block` data class called `new_block`
    # Use the user input from Step 2 for the `data` attribute
    # Use the integer 42 for the `creator_id`
    new_block = Block(data=input_data, creator_id=42)
    # Use the `st.write` function to display the new block.
    st.write(new_block)

################################################################################
# Step 4:
# Test the Application

# Complete the following steps:
# 1. In the terminal, navigate to the `Unsolved` folder for this activity.
# 2. Be sure that your Conda development environment is active.
# 3. Run the Streamlit app in the terminal by using `streamlit run app.py`.
# 4. Type some input text in the text box, and then click the Add Block button.
# 5. Confirm that an instance of the `Block` class that appears on the page.

################################################################################
