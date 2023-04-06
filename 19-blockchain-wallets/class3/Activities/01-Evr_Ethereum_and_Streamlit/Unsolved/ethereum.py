# Ethereum Account Functions

################################################################################

# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
################################################################################

# Create a function called `generate_account` that automates the Ethereum
# account creation process
# Access the mnemonic phrase from the `.env` file
# Create Wallet object instance
# Derive Ethereum private key
# Convert private key into an Ethereum account
# Return the account from the function
