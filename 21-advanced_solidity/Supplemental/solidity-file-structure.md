There is no one-size-fits-all answer to this question, as the best file structure for installing and importing NPM libraries for Solidity will depend on the specific needs of your project. That being said, here are some general recommendations for structuring your project:

1. Root Directory: This should contain an NPM `package.json` file.

2. `contracts` directory: This directory should contain all of your Solidity contracts.

3. `build` directory: This directory can be used to store compiled contract artifacts, which can be useful for deployment and testing.

4. `test` directory: This directory should contain all of your test files and scripts.

5. `migrations` directory: This directory can be used to store migration scripts for deploying your contracts to a local development network or a public Ethereum network.

When it comes to installing and importing NPM libraries for Solidity, it is generally best to install them as local dependencies within your project. This will ensure that library versions remain consistent across all environments, and will make it easier to share your project with others.

When installing NPM libraries, you can specify the `--save` flag to add them to your `package.json` file, like so:
```
npm install --save my-solidity-library
```

To import the library in your Solidity contracts, you can use the `import` statement at the top of each file, like so:
```
import "./path/to/my-solidity-library/ContractName.sol";
```

Note that the specific path to the contract will depend on the file structure of your project. You can use relative or absolute paths, as long as they point to the correct file.