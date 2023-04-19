/*
Arcade Token
*/

// Construct your ArcadeToken contract below:

// SPDX-License-Identifier: MIT
pragma solidity ^0.8;

contract ArcadeToken {
    address owner = msg.sender;
    bytes5 public symbol = "MNSTR";
    uint128 public exchange_rate = 1 * 10**18;
    
    mapping(address => uint) public balances;

    function balance() public view returns (uint) {
        return balances[msg.sender];
    }

    function transfer(address recipient, uint value) public {
        balances[msg.sender] -= value;
        balances[recipient] += value;
    }

    function purchase() public payable {
        uint _value = msg.value;
        uint amount = _value * exchange_rate;
        balances[msg.sender] += amount;
        // Send value to owner?
        payable(owner).transfer(_value);
    }

    function mint(address recipient, uint value) public {
        require(msg.sender==owner, "Only the owner can mint tokens.");
        balances[recipient] += value;
    }


}