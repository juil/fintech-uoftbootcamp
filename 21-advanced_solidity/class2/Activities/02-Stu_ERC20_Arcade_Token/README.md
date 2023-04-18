# ERC-20 Arcade Token

In this activity, you’ll create an `ArcadeToken` smart contract by using the `ERC20` and `ERC20Detailed` smart contracts that the OpenZeppelin library provides.

## Instructions

1. Open the Remix IDE, and then create a new file named `ArcadeTokenERC20.sol`.

    > **Note** You can copy the contents of this starter file for this activity into the new `ArcadeTokenERC20.sol` file to help you get started.

2. Set the `pragma` to any version from 0.5.0 to 0.5.17.

3. Import the `ERC20` and `ERC20Detailed` contracts from OpenZeppelin. (These contracts implement the ERC-20 standards that you’ll use to build your arcade contract.) Import these contracts by using the following code:

    ```solidity
    import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
    import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
    ```

4. Define a contract named `ArcadeToken` that inherits the OpenZeppelin `ERC20` and `ERC20Detailed` contracts.

5. Add an `address payable` variable named `owner`.

6. Use the following code to create an `onlyOwner` modifier:

    ```solidity
    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
         _;
    }
    ```

    > **Note** You’ll use this code later to restrict who can mint new tokens.

7. Use the following code to create a constructor that will configure the `ArcadeToken` contract and the `ERC20Detailed` contract:

    ```solidity
    constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }
    ```

8. Create a function named `mint` that accepts a recipient address and an amount. Restrict this function to the contract owner by using the `onlyOwner` modifier that you created earlier. To do all this, use the following code:

    ```solidity
    function mint(address recipient, uint amount) public onlyOwner {
        _mint(recipient, amount);
    }
    ```

9. Test your contract by deploying it and then calling the functions that the Remix IDE exposes. Try minting some tokens for yourself and then sending them to another address.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

