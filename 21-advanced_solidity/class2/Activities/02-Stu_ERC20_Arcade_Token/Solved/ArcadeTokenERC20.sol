/*
ERC-20 Arcade Token

Instructions:

1. Open Remix, and create a new file called `ArcadeTokenERC20.sol`.

> **Note** You can copy the contents of this activity’s starter file into Remix to help you get started.

2. Set the pragma to any version from 0.5.0 to 0.5.17.

3. Import the `ERC20` and `ERC20Detailed` contracts from OpenZeppelin. These contracts implement the `ERC20` standards that we’ll use to build our arcade contract. Import these contracts by using the following code:

```solidity
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
```

4. Define a contract named `ArcadeToken` that inherits the OpenZeppelin `ERC20` and `ERC20Detailed` contracts.

5. After you define your contract and name it `ArcadeToken`, add an `address payable` variable called `owner`.

5. Next, use the following code to create an `onlyOwner` modifier. This code will later be used to restrict who can mint new tokens.

```solidity
modifier onlyOwner {
    require(msg.sender == owner, "You do not have permission to mint these tokens!");
     _;
}
```

6. Use the following code to create a constructor that will configure the `ArcadeToken` contract and the `ERC20Detailed` contract:

```solidity
constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
    owner = msg.sender;
    _mint(owner, initial_supply);
}
```

7. Finally, create a function called `mint` that accepts a recipient address and amount. Restrict this function to the contract owner by using the `onlyOwner` modifier that you created earlier. To do so, use the following code:

```solidity
function mint(address recipient, uint amount) public onlyOwner {
    _mint(recipient, amount);
}
```

8. Test out your contract by deploying it and calling the functions that Remix exposes. Try minting some tokens for yourself, then sending them to another address!

*/

pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract ArcadeToken is ERC20, ERC20Detailed {
    address payable owner;

    modifier onlyOwner {
        require(msg.sender == owner, "You do not have permission to mint these tokens!");
        _;
    }

    constructor(uint initial_supply) ERC20Detailed("ArcadeToken", "ARCD", 18) public {
        owner = msg.sender;
        _mint(owner, initial_supply);
    }

    function mint(address recipient, uint amount) public onlyOwner {
        _mint(recipient, amount);
    }
}
