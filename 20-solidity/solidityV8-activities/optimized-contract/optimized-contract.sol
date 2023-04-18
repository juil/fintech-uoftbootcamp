    //SPDX-License-Identifier: Unlicense
    pragma solidity ^0.8.0;

    contract OptimizedContract {
        struct Person {
     	  /* Add constructor with two variable name and age*/
          // Optimize: Pack variables
          uint8 age;
          string name;
        }

        Person[] public people;

        /* Add a function addperson with name and age */
        function addPerson(string memory _name, uint8 _age) public {
            people.push(
                Person ({
                    name: _name,
                    age: _age
                })
            );
        }

        function getPerson(uint index) public view returns (Person memory) {
            /* Add a function getPerson with name and age */
            // If returning type bytes
            // bytes memory encoded = abi.encode(people[index]);
            // return encoded;
            return people[index];
        }
    }