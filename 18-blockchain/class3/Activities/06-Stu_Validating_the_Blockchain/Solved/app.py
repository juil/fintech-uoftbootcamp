# Validating the Blockchain
################################################################################
# In this activity, you’ll update your `PyChain` application with a method that
# validates the entire blockchain.

################################################################################
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib

################################################################################
# Creates the Block and PyChain data classes


@dataclass
class Block:
    data: Any
    creator_id: int
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    prev_hash: str = "0"
    nonce: int = 0

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

@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):

        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):

        # Step 1:
        # Write the code that validates the integrity of the PyChain by
        # comparing the calculated hash code of each block to the `prev_hash`
        # value contained in the following block.

        # Add the code to generate the hash of the first block in the chain.
        # Set the hash equal to a variable called block_hash
        # Hint - The first block in the chain is at index position 0.
        block_hash = self.chain[0].hash_block()

        # Create a for-loop to access the remainder of the blocks in the
        # chain, starting at index position 1
        for block in self.chain[1:]:

            # Code an if statement that compares the block_hash of the
            # previous block to the prev_hash value of the current block
            # If the two hashes are NOT equal, print a statement that says
            # "Blockchain is invalid", and then return the value False
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            # Set the block_hash value equal to the hashed value of the current
            # block
            block_hash = block.hash_block()

        print("Blockchain is Valid")
        return True

################################################################################
# Streamlit Code

# Adds the cache decorator for Streamlit


@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block(data="Genesis", creator_id=0)])


pychain = setup()


st.markdown("# PyChain")
st.markdown("## Store a Record in the PyChain")

input_data = st.text_input("Block Data")

################################################################################

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 4)

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
# Step 2:
# Add a button with the text “Validate Blockchain” to your Streamlit interface.

# Add a button with the text “Validate Blockchain” to your Streamlit interface.
if st.button("Validate Blockchain"):

    # Step 3:
    # Code the Validate Blockchain button so that when it’s clicked, it calls
    # the `is_valid` method of the `PyChain` data class and then writes the
    # result to the webpage.

    # Call the `is_valid` method of the `PyChain` data class and `write` the
    # result to the Streamlit interface
    st.write(pychain.is_valid())

################################################################################
# Step 4:
# Test the application.

# Complete the following steps:
# 1. In the terminal, navigate to the `Unsolved` folder for this activity.
# 2. Be sure that your Conda development environment is active.
# 3. Run the Streamlit app in the terminal by using `streamlit run app.py`.
# 4. Type some input text in the text box, and then click the Add Block button.
# This adds a block to the chain. Repeat this process.
# 5. Click the Validate Blockchain button to validate the current ledger.

################################################################################
