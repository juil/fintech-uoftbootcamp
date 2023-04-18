    //SPDX-License-Identifier: Unlicense
    pragma solidity ^0.8.0;

    contract OptimizedContract {
        struct Person {
     	  /* Add constructor with two variable name and age*/
          string name;
          uint age;
        }

        Person[] public people;

        /* Add a function addperson with name and age */
        function addPerson(string memory _name, uint _age) public {
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