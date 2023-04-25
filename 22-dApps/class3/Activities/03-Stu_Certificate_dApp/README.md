# Building a Certificate dAPP

In this activity, you’ll create a dApp for the certificate contract.

## Instructions

The instructions for this activity are divided into the following steps:

1. Deploy the contract.

2. Load the contract.

3. Complete the “Award Certificate” section.

4. Complete the “Display Certificate” section.

### Step 1: Deploy the Contract

1. Deploy the [awardCertificate token](./Unsolved/contracts/certificate.sol) by using the Remix IDE, MetaMask, and Ganache.

2. Copy the `SAMPLE.env` file to a file named `.env`, and then update the file with the address of your deployed contract.

3. Copy the contract's ABI file into a JSON file.

### Step 2: Load the Contract

In the `app.py` file, in the "Contract Helper function" section, complete the following steps:

1. Load the certificate token's compiled ABI JSON file.

2. Use the `dotenv` library to set the contract's address by loading the value from the `.env` file.

3. Connect to the contract by using Web3.py.

### Step 3: Complete the “Award Certificate” Section

In the `app.py` file, in the "Award Certificate" section, complete the following steps:

1. Add the Streamlit component that’s needed for entering the address of the certificate recipient.

2. Add the Streamlit component that’s needed for entering either a link or a string of text for a certificate.

    > **Hint** You can generate a fake certificate by using a free online service and then link to this certificate. Or, you can accept a string of text, like "FinTech Certificate of Completion".

3. Use the Web3.py `contract.functions` object to perform a transaction on the `awardCertificate` contract function.

### Step 4: Complete the “Display Certificate” Section

In the `app.py` file, in the "Display Certificate" section, complete the following steps:

* Use the Web3.py `contract.functions` object and `certificate_id` to get `ownerOf` for the certificate.

* Use the Web3.py `contract.functions` object and `certificate_id` to get `tokenURI` for the certificate.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
