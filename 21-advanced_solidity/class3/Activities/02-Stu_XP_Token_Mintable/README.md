# XP_Token Mintable

In this activity, you’ll generate the code for the `XP_Token` contract.

This contract will inherit functionality from the OpenZeppelin `ERC20`, `ERC20Detailed`, and `ERC20Mintable` contracts.

## Instructions

1. Navigate to the Remix IDE, and then create a new smart contract file named `XPTokenMintable.sol`.

2. Add the `pragma` line at the beginning of the file. The pragma version can range from `^0.5.0;` to `^0.5.17;`

3. Add `import` statements for the `ERC20`, `ERC20Detailed`, and `ERC20Mintable` contracts from GitHub.

4. Define a contract named `XP_Token` that inherits the `ERC20`, `ERC20Detailed`, and `ERC20Mintable` contracts.

5. Inside the `XP_Token` contract, create a constructor function that details the following three attributes:

    * `string memory name`

    * `string memory symbol`

    * `uint initial_supply`

6. Inside the constructor function, include the `ERC20Detailed` constructor. Note that the `ERC20Detailed` constructor includes parameters for the `name` and the `symbol` (both of which will get defined at contract deployment), and the value 18 (which will detail the number of associated decimal places). Make this function public.

7. Add the body of the constructor. Call the `mint` function, passing it the parameters for the `msg.sender` and the `initial_supply` of tokens.

8. In the Remix IDE, navigate to the **Solidity compiler** pane.

8. In the Compiler drop-down list, select any version from 0.5.0 to 0.5.17, and then click the Compile button.

10. Check for any errors, and debug them as needed.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.