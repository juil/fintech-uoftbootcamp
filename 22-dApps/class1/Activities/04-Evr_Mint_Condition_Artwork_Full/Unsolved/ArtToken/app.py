import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# The Load_Contract Function
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    # @TODO: YOUR CODE HERE!

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    # @TODO: YOUR CODE HERE!

    return contract


contract = load_contract()


################################################################################
# Register New Artwork
################################################################################
st.title("Register New Artwork")

accounts = w3.eth.accounts

# Use a Streamlit component to get the address of the artwork owner from the user
# @TODO: YOUR CODE HERE!

# Use a Streamlit component to get the artwork's URI
# HINT: You can just enter this as text for now.
# @TODO: YOUR CODE HERE!

if st.button("Register Artwork"):

    # Use the contract to send a transaction to the registerArtwork function
    tx_hash =  # @TODO: YOUR CODE HERE!

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")


################################################################################
# Display a Token
################################################################################
st.markdown("## Check Balance of an Account")

selected_address = st.selectbox("Select Account", options=accounts)

tokens = contract.functions.balanceOf(selected_address).call()

st.write(f"This address owns {tokens} tokens")

st.markdown("## Check  Ownership and Display Token")

total_token_supply = contract.functions.totalSupply().call()

token_id = st.selectbox("Artwork Tokens", list(range(total_token_supply)))

if st.button("Display"):

    # Get the art token owner
    owner =  # @TODO: YOUR CODE HERE!
    
    st.write(f"The token is registered to {owner}")

    # Get the art token's URI
    token_uri = # @TODO: YOUR CODE HERE!

    st.write(f"The tokenURI is {token_uri}")
    st.image(token_uri)

