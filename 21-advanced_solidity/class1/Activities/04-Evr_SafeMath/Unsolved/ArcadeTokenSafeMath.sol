/*
SafeMath
*/

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// @TODO: import the SafeMath library via Github URL
import "./node_modules/@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ArcadeToken {
    // @TODO: add the "using SafeMath..." line here to link the library to all uint types
    using SafeMath for uint;

    address owner = msg.sender;
    string public symbol = "ARCD";
    uint public exchange_rate = 100;

    mapping(address => uint) balances;

    function balance() public view returns(uint) {
        return balances[msg.sender];
    }

    function transfer(address recipient, uint value) public {
        // @TODO: replace the following with the .sub function
        balances[msg.sender] = balances[msg.sender].sub(value);
        // @TODO: replace the following with the .add function
        balances[recipient] = balances[recipient].add(value);
    }

    function purchase() public payable {
        // @TODO: replace the following with the .mul function
        uint amount = msg.value.mul(exchange_rate);
        // @TODO: replace the following with the .add function
        balances[msg.sender] = balances[msg.sender].add(amount);
        payable(owner).transfer(msg.value);
    }

    function mint(address recipient, uint value) public {
        require(msg.sender == owner, "You do not have permission to mint tokens!");
        // @TODO: replace the following with the .add function
        balances[recipient] = balances[recipient].add(value);
    }
}
