# Dynamic Difficulty
################################################################################
# In this activity, you’ll test the integration of the proof of work consensus 
# mechanism in your PyChain application.

################################################################################
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

################################################################################
# Creates the Block data class

@dataclass
class Block:
    data: Any
    creator_id: int
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    prev_hash: str = "0"
    nonce: str = 0

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        creator_id = str(self.creator_id).encode()
        sha.update(data)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()

################################################################################
# Step 1:
# Add a `difficulty` data attribute to the `PyChain` data class.
# Use a data type of `int` and a default value of 4.


@dataclass
class PyChain:
    chain: List[Block]

    # Add a `difficulty` data attribute with a data type of `int` and a default
    # value of 4.
    difficulty: int = 4

# Step 2:
# Add a `num_of_zeros` data attribute that multiplies the string value ("0") by 
# the `difficulty` value.
    def proof_of_work(self, block):
        calculated_hash = block.hash_block()

        # Add a `num_of_zeros` data attribute that multiplies the string value ("0") 
        # by the `difficulty` value.
        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):
            block.nonce += 1
            calculated_hash = block.hash_block()

        print("Winning Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit
@st.cache(allow_output_mutation=True)

def setup():
    print("Initializing Chain")
    return PyChain([Block(data="Genesis", creator_id=0)])


pychain = setup()

st.markdown("# PyChain")
st.markdown("## Store Data in the Chain")

input_data = st.text_input("Block Data")

################################################################################
# Step 3:
# Add a Streamlit component that can update the `difficulty` attribute of the 
# `PyChain` class. To do so, complete the following steps:
# 1. Add a Streamlit slider component that allows the user to select a difficulty 
# value from 1 to 5. Set the starting value to 4. Set this component equal to a 
# variable named `difficulty`.
# 2.Update the `difficulty` data attribute of the `PyChain` data class 
# (`pychain.difficulty`) with this new `difficulty` value.

# Add a Streamlit slider named "Block Difficulty" that allows the user to update a 
# difficulty value. Set this equal to the variable `difficulty`
difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 4)

# Update the `difficulty` data attribute of the `PyChain` data class (`pychain.difficulty`) 
# with this new `difficulty` value
pychain.difficulty = difficulty


if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    new_block = Block(data=input_data, creator_id=42, prev_hash=prev_block_hash)

    pychain.add_block(new_block)

    st.write("Winning Hash", new_block.hash_block())

st.markdown("## PyChain Ledger")
pychain_df = pd.DataFrame(pychain.chain)

st.write(pychain_df)


################################################################################
# Step 4:
# Test the application.

# Complete the following steps:
# 1. In the terminal, navigate to the `Unsolved` folder for this activity.
# 2. Be sure that your Conda development environment is active.
# 3. Run the Streamlit app in the terminal by using `streamlit run app.py`.
# 4. Create a new block in the Streamlit interface and confirm that it is added to the PyChain.
# 5. Change the difficulty, and then add another block. Observe how this affects the overall mining time (the time that it takes to add a block to the
# chain with the proof of work enabled).

################################################################################
