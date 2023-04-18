    //SPDX-License-Identifier: Unlicense
    pragma solidity ^0.8.0;

    contract OptimizedContract {
        struct Person {
     	  /* Add constructor with two variable name and age*/
          bytes32 name;
          uint8 age;
        }

        Person[] public people;

        function addPerson(string memory _name, uint _age) 

	  /* Add a function addperson with name and age */

        function getPerson(uint index) public view returns (bytes memory) {
     
	 /* Add a function getPerson with name and age */	

        }
    }