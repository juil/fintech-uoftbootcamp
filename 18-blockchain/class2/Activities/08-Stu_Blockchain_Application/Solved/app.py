# Blockchain Application
################################################################################
# In this activity, you’ll build a Streamlit application that can both generate
# new blocks of user data and add them to a Python blockchain.

# You will need to complete the following steps:
# 1. Review the starter code included for both the `Block` data class and the
# Streamlit application.
# 2. Modify the "Add Block" button below to add new blocks to the blockchain.
# 3. Display the blockchain data.
# 4. Test the application.
################################################################################
# Imports
import streamlit as st
import datetime as datetime
from dataclasses import dataclass
from typing import Any, List
import pandas as pd
import datetime as datetime
import hashlib

################################################################################
# Step 1:
# Review the provided code in the `app.py` file for both the `Block` data class
# and the Streamlit web application. This mirrors what you created in a prior
# activity.

################################################################################
# Creates the Block and PyChain data classes


@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        return sha.hexdigest()

# Create the data class PyChain


@dataclass
class PyChain:
    chain: List[Block]

    def add_block(self, block):
        self.chain += [block]

################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit


@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block(data="Genesis", creator_id=0)])


pychain = setup()

st.markdown("# PyChain: A Python Blockchain Application")
st.markdown("## Store Data in the Chain")
st.sidebar.markdown("### New Block Hash")

input_data = st.text_input("Block Data")

################################################################################
# Step 2:
# Modify the Streamlit “Add Block” button code so that when someone clicks the
# button, the code adds a new block to the blockchain.

# Include the following steps:
# 1. Select the previous block in the chain by using the following
# code:`prev_block = pychain.chain[-1]`.
# 2. Hash the previous block by using the following
# code: `prev_block_hash = prev_block.hash_block()`.
# 3. Create a new block by using the following
# code: `new_block = Block(data=input_data, creator_id=42, prev_hash=prev_block_hash)`
# 4. Add the new block to the chain by using the following
# code: `pychain.add_block(new_block)`.

if st.button("Add Block"):

    # Select the previous block in the chain
    prev_block = pychain.chain[-1]

    # Hash the previous block in the chain
    prev_block_hash = prev_block.hash_block()

    # Create a new block in the chain
    new_block = Block(data=input_data, creator_id=42, prev_hash=prev_block_hash)

    # Add the new block to the chain
    pychain.add_block(new_block)

################################################################################
# Step 3:
# Display the the `PyChain` ledger data on the Streamlit webpage
# 1. Create a Pandas DataFrame so that the block data will display in a more user-friendly 
# manner. To do so, use the following code: `pychain_df = pd.DataFrame(pychain.chain)`
# 2. Write the Pandas DataFrame to the screen by using the `st.write` function.


st.markdown("## PyChain Ledger")

# Create a Pandas DataFrame to display the `PyChain` ledger
pychain_df = pd.DataFrame(pychain.chain)

# Use the Streamlit `write` function to display the `PyChain` DataFrame
st.write(pychain_df)

################################################################################
# Step 4:
# Test the application.

# Complete the following steps:
# 1. In the terminal, navigate to the `Unsolved` folder for this activity.
# 2. Be sure that your Conda development environment is active.
# 3. Run the Streamlit app in the terminal by using `streamlit run app.py`.
# 4. Adjust the input text in the text box, and then click the Add Block button.
# 5. Review the changes in the `PyChain` ledger that the Streamlit application
# webpage reflects.

################################################################################
