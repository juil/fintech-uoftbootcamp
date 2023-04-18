// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Fallback {
    event Log(string func, uint gas);

    // Fallback function must be declared as external.
    fallback() external payable {
        // send / transfer (forwards 2300 gas to this fallback function)
        // call (forwards all of the gas)
        // Enter CODE HERE
    }

    // Receive is a variant of fallback that is triggered when msg.data is empty
    receive() external payable {
        // Enter CODE HERE
    }

    // Helper function to check the balance of this contract
    function getBalance() public view returns (uint) {
        // Enter CODE HERE
    }
}

contract SendToFallback {
    function transferToFallback(address payable _to) public payable {
        // Enter CODE HERE
    }

    function callFallback(address payable _to) public payable {
        // Enter CODE HERE
    }
}
