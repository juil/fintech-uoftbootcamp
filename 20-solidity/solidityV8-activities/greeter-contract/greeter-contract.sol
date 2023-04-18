//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;
// import "./hardhat/console.sol";
contract Greeter {
    string private greeting;
    

    /* create constructor that take a paramter, and assigns to greeting that was creaed earlier */
    constructor(string memory _greeting) {
        greeting = _greeting;
    }

    function greet() public view returns (string memory) {
        return greeting;
    }

    function setGreeting(string memory _greeting) public {
	    // Create function to changing greeter 
        greeting = _greeting;
    }
}