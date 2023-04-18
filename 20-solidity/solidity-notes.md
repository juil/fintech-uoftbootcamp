# Solidity Notes

## Optimization

[Gas Optimization](https://eip2535diamonds.substack.com/p/smart-contract-gas-optimization-with)
Gas optimization is a matter of doing what is cheap and avoiding what is expensive in terms of gas costs on EVM blockchains.

What is **cheap**:

* Reading constants and immutable variables.
* Reading and writing local variables.
* Reading and writing memory variables like memory arrays and structs.
* Reading calldata variables like calldata arrays and structs.
* Internal function calls.

What is **expensive**:

* Read and writing state variables that are stored in contract storage.
* External function calls.
* Loops

## Breaking Changes 

- `// SPDX-License-Identifier: MIT`
- `address` is not explicitly `payable`
- default `function()` is now

```solidity 
fallback() external payable {}
receive() external payable {}
```
