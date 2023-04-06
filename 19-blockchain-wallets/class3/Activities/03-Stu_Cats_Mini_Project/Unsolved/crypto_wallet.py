# Imports
import os
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account, Web3
from web3.gas_strategies.time_based import medium_gas_price_strategy

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))


# Wallet functionality

#@TODO create a function called generate account do not forget to add each of the following steps

def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.
    
    # Create Wallet Object
   
    # Derive Ethereum Private Key
 
    # Convert private key into an Ethereum account

    return account
    
#@TODO create a function called generate account do not forget to add each of the following steps
def get_balance(address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance of address in Wei
 
    # Convert Wei value to ether

    # Return the value in ether
    return ether

