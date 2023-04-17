# Solidity Notes

## Breaking Changes 

- `// SPDX-License-Identifier: MIT`
- `address` is not explicitly `payable`
- default `function()` is now

```solidity 
fallback() external payable {}
receive() external payable {}
```
