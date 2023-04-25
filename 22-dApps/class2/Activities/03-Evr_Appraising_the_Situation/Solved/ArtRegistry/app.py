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
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/artregistry_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()


st.title("Art Registry Appraisal System")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

################################################################################
# Register New Artwork
################################################################################
st.markdown("## Register New Artwork")

artwork_name = st.text_input("Enter the name of the artwork")
artist_name = st.text_input("Enter the artist name")
initial_appraisal_value = st.text_input("Enter the initial appraisal amount")
artwork_uri = st.text_input("Enter the URI to the artwork")

if st.button("Register Artwork"):
    tx_hash = contract.functions.registerArtwork(
        address,
        artwork_name,
        artist_name,
        int(initial_appraisal_value),
        artwork_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")


################################################################################
# Appraise Art
################################################################################
st.markdown("## Appraise Artwork")
tokens = contract.functions.totalSupply().call()
token_id = st.selectbox("Choose an Art Token ID", list(range(tokens)))
new_appraisal_value = st.text_input("Enter the new appraisal amount")
report_uri = st.text_area("Enter notes about the appraisal")
if st.button("Appraise Artwork"):

    # Use the token_id and the report_uri to record the appraisal
    tx_hash = contract.functions.newAppraisal(
        token_id,
        int(new_appraisal_value),
        report_uri
    ).transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write(receipt)
st.markdown("---")

################################################################################
# Get Appraisals
################################################################################
st.markdown("## Get the appraisal report history")
art_token_id = st.number_input("Artwork ID", value=0, step=1)
if st.button("Get Appraisal Reports"):
    appraisal_filter = contract.events.Appraisal.createFilter(
        fromBlock=0,
        argument_filters={"tokenId": art_token_id}
    )
    appraisals = appraisal_filter.get_all_entries()
    if appraisals:
        for appraisal in appraisals:
            report_dictionary = dict(appraisal)
            st.markdown("### Appraisal Report Event Log")
            st.write(report_dictionary)
            st.markdown("### Appraisal Report Details")
            st.write(report_dictionary["args"])
    else:
        st.write("This artwork has no new appraisals")
