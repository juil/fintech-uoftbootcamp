# Sending Remittances

In this activity, you’ll deploy and run the `CustomerAccount` contract that you created in earlier lessons to send remittances by using smart contracts.

## Background

It’s now time to put your remittances prototype into action! You’ve been asked to present a demo during the next board meeting. So, you decide to run this demo by using the sandboxed environment that the JavaScript VM of the Remix IDE provides.

## Instructions

1. Open the Remix IDE. Create a new Solidity file to code your smart contract. You can either copy and paste the code from the provided `customer_account.sol` starter file, or reuse the code from the `customer_account.sol` file that you created during the last class. 

2. Compile your smart contract. If an error occurs, review your code, and make the necessary changes for a successful compilation.

3. Navigate to the “Deploy & Run Transactions” pane, and then deploy your contract.

4. Run the `getInfo` function, and then review the output that the Remix IDE displays.

5. Use the `setInfo` function to fulfill the required customer information in the contract. Set an initial account balance of zero.

    > **Note:** You can either create new, dummy addresses on the [Vanity-ETH](https://vanity-eth.tk/) website, which includes an Ethereum vanity address generator, or use the following Ethereum addresses:
    >
    > ```text
    > Dummy owner address: 0x0c0669Cd5e60a6F4b8ce437E4a4A007093D368Cb
    > Dummy authorized recipient address: 0x7A1f3dFAa0a4a19844B606CD6e91d693083B12c0
    > ```

6. Run the `getInfo` function for a second time, and then review the output that the Remix IDE displays.

7. Use the `deposit` function to add 20 ether to the contract. 
  
    * Demonstrate that adding a value to the account via the `value` box under the gas limit will allow the ether to be used in the simulation.

8. Run the `accountBalance` function, and then review the output that the Remix IDE displays.

    > **Note:** Did you notice anything interesting? You never coded a function named `accountBalance`. However, it’s available as a function for the deployed contract! This is a getter function that the Solidity compiler automatically generated, because the `accountBalance` variable is public.

9. Use the `sendRemittance` function to send a remittance of 5 ether to either the account owner address or the authorized recipient address.

10. Run the `getInfo` function for the third time, and then review the output that the Remix IDE displays.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

