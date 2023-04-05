# Blockchain Transactions Install Guide

This guide serves as a step-by-step process for setting up and validating the tools you will use in this unit. Without these libraries, class activities and their associated code, you will not be able to perform the necessary operations.

## Installation Process

Welcome to Module 19! In this Getting Started guide, you’ll set up the tools you’ll need for this module, which include:

* [Web3.py](https://web3py.readthedocs.io/en/stable/overview.html): A Python library for connecting to and performing operations on Ethereum-based blockchains.

* [ethereum-tester](https://pypi.org/project/ethereum-tester/0.1.0a4/): A Python library that provides access to the tools we’ll use to test Ethereum-based applications.

* [mnemonic](https://pypi.org/project/mnemonic/): A Python implementation for generating a 12- or 24-word mnemonic seed phrase based on the BIP-39 standard.

* [bip44](https://pypi.org/project/bip44/): A Python implementation for deriving hierarchical deterministic wallets from a seed phrase based on the BIP-44 standard.

### Set Up Python Modules and Libraries

To install the **Web3.py**  library, check that your `dev` environment is active, and then run the following:

```shell
pip install web3==5.17
```

To install the **ethereum-tester** library, check that your `dev` environment is active, and then run the following:

```shell
pip install eth-tester==0.5.0b3
```

To install the **mnemonic** package, check that your `dev` environment is active, and then run the following:

```shell
pip install mnemonic
```

To install the **bip44**  package, check that your `dev` environment is active, and then run the following:

```shell
pip install bip44
```

### Extra Python Modules

Install:

- [`eth-rlp`](https://anaconda.org/conda-forge/eth-rlp)
- [py-evm](https://py-evm.readthedocs.io/en/latest/guides/quickstart.html)

```shell
pip install py-evm
conda install -c conda-forge eth-rlp
```

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
