// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0;

contract MySimpleStorage{


    struct People{
        string name;
        int age;
    }

    People [] people;

    // add people
    function addPerson(string memory _name, int _age) public{
        people.push(People(_name, _age));
    }

    // get people
    function getPerson(uint256 index) public view returns(string memory, int){
        return (people[index].name, people[index].age);
    }
}