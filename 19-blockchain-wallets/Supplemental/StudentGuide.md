# Unit 19: Blockchain Wallets

## Getting Started

* [Web3.py](https://web3py.readthedocs.io/en/stable/overview.html): A Python library for connecting to and performing operations on Ethereum-based blockchains.

* [ethereum-tester](https://pypi.org/project/ethereum-tester/0.1.0a4/): A Python library that provides access to the tools we’ll use to test Ethereum-based applications.

* [mnemonic](https://pypi.org/project/mnemonic/): A Python implementation for generating a 12- or 24-word mnemonic seed phrase based on the BIP-39 standard.

* [bip44](https://pypi.org/project/bip44/): A Python implementation for deriving hierarchical deterministic wallets from a seed phrase based on the BIP-44 standard.

## Helpful Links

<details><summary>Blockchain</summary>

* https://www.investopedia.com/terms/b/blockchain.asp
</details>

<details><summary>Nodes</summary>

* https://medium.com/coinmonks/blockchain-what-is-a-node-or-masternode-and-what-does-it-do-4d9a4200938f
</details>
<details><summary>Blockchain Wallets</summary>

* https://www.investopedia.com/terms/b/blockchain-wallet.asp

* https://blog.unocoin.com/what-happens-if-you-forget-your-bitcoin-wallet-keys-bbf563ce281a
</details>
<details><summary>Digital Signature</summary>

* https://www.instantssl.com/digital-signature

* https://medium.com/@xragrawal/digital-signature-from-blockchain-context-cedcd563eee5
</details>
<details><summary>Hash</summary>

* https://www.investopedia.com/terms/h/hash.asp
</details>
<details><summary>Blockchain Mining</summary>

* https://www.bitcoinmining.com/
</details>
<details><summary>Consensus Algorithms</summary>

* https://www.binance.vision/blockchain/what-is-a-blockchain-consensus-algorithm
</details>
<details><summary>Proof of Authority</summary>

* https://www.binance.vision/blockchain/proof-of-authority-explained
</details>
<details><summary>Proof of Work</summary>

* https://en.bitcoin.it/wiki/Proof_of_work
</details>
<details><summary>Proof of Stake</summary>

* https://www.investopedia.com/terms/p/proof-stake-pos.asp
</details>

### Set Up Python Modules and Libraries

To install the **Web3.py**  library, check that your `dev` environment is active, and then run the following:

```shell
pip install web3==5.17
```

To install the **ethereum-tester** library, check that your `dev` environment is active, and then run the following:

```shell
pip install eth-tester
```

To install the **mnemonic** package, check that your `dev` environment is active, and then run the following:

```shell
pip install mnemonic
```

To install the **bip44**  package, check that your `dev` environment is active, and then run the following:

```shell
pip install bip44
```
## Reflection

Congratulations on completing another module! This week’s material was challenging but important. You now have knowledge of cutting-edge technology, and the ability to use and interact with a real blockchain network. This is a valuable addition to your fintech skillset.

You can now perform the following tasks:

*  Explain what a blockchain transaction is and how it applies to fintech and the financial industry.

* Connect to an Ethereum blockchain using the Web3.py library.

* Understand the basics of asymmetric cryptography and public-private key pairs.

* Generate a digital wallet from a mnemonic seed phrase.

* Sign a transaction by using a blockchain account’s private key.

* Verify a transaction by using a blockchain account’s public key and account address.

* Sign and execute a transaction on a test blockchain network by using Web3.py.

* Analyze blockchain transactions by using a blockchain explorer.

---
## Key Links

To learn more about working with Web3.py and the Ethereum blockchain, review the following resources:

* [Web3.py](https://web3py.readthedocs.io/en/stable/index.html)

* [Ethereum](https://ethereum.org/en/what-is-ethereum/)

* [Ethereum for Python Developers](https://ethereum.org/en/developers/docs/programming-languages/python/)

---
## Summary

<details><summary>What is a Public Key, Private Key and Nonce?</summary><br>

**Public Key** - A public key is a key that is provided publicly to others to use in conjunction with another person's private key to decrypt and encrypt messages securely.

**Private Key** - A private key is a key that is kept secret. It can be used in conjunction with another person's public key to encrypt and decrypt messages with asymmetric cryptography or it can be shared with another person so that they might decrypt your symmetric cryptography message.

**Nonce** - A nonce is a number used once. It can be added to cryptographic methods to increase security by introducing an element of randomness.

The uses of these terms is explained in more detail in the next question: *What is the difference between Symmetric and Asymmetric Cryptography?*.

</details>

<details><summary>What is the difference between Symmetric and Asymmetric Cryptography, and how is it related to nonce and digital signatures?</summary><br>

Symmetric cryptography means "one key" to "one lock" -- hence the "symmetry." Asymmetric cryptography doesn't just use one key like symmetric, but now it splits up the key into a "keypair" -- a public key and a private key, or "two keys" to "one lock."

With symmetric cryptography, the private key is shared between the parties in need of the message. The key encrypts and decrypts the message.

Asymmetric cryptography uses a public key *and* a private key to encrypt/decrypt messages.

To **encrypt** and send a message:
-- The sender must have their own private key, and the _recipient's_ public key.

To **decrypt** a received message:
-- The recipient must have their own private key, and the _sender's_ public key.

Using a nonce with this method can increase security by adding an element of randomness. The Nonce, _number used once_, is used to make the resulting encrypted message different regardless of the same input, which makes it harder to analyze the output for patterns. If employing the nonce method with your cryptographic algorithm, it would be required to regenerate the same results again later or to decrypt data properly.

Digital signatures are the use of a private key to digitally 'sign' a document. To sign a document digitally, one must use their private key to "sign" the data which produces a string of alphanumeric characters. This string is the "signature." The recipient of the document can then use the public key of the signer to verify that the signature and document was not tampered with.

To read more about digital signatures, click [here](https://www.instantssl.com/digital-signature) and [here](https://medium.com/@xragrawal/digital-signature-from-blockchain-context-cedcd563eee5).

</details>

<details><summary>What are consensus algorithms?</summary><br>

Consensus algorithms in blockchain are methods to allow the network to reach agreement (consensus!) on whether a block can be trusted and thus added to the chain. Because blockchains are decentralized, no one person can be trusted to make this decision, so consensus algorithms are used. These algorithms typically use some type of collateral structure to determine trustworthiness. For more information on consensus algorithms in general, check out [this article](https://www.binance.vision/blockchain/what-is-a-blockchain-consensus-algorithm).

The three main types of consensus algorithms that we cover in class are:

<blockquote>

<details><summary>Proof of Authority</summary><br>

- This algorithm deviates somewhat from the decentralized nature of blockchains in that there are designated entities that validate the blocks. PoA is almost always used for test networks and not for production.
- With this algorithm, the entities put their reputation on the line as collateral and must typically be voted in.
- For more information on *PoA*, check out [this article](https://www.binance.vision/blockchain/proof-of-authority-explained).
</details>

<details><summary>Proof of Work</summary><br>

- Used by Bitcoin and many other well known blockchains, *Proof of Work* was the first consensus algorithm used in a public blockchain, and is where the term *mining* originated.
- To maliciously attack a blockchain using *PoW*, one would need to use 51% of the computational power that the network uses. This strongly disincentivizes attacking the network.
- With this algorithm, the entities put their computational resources on the line as collateral.
- For more information on *PoW*, check out [this article](https://en.bitcoin.it/wiki/Proof_of_work).
</details>
<details><summary>Proof of Stake</summary><br>

- Developed as alternative to the resource intensive *PoW* algorithm, this method validates blocks based on a monetized stake in the network.
- To maliciously attack a blockchain using *PoS*, one would need to hold 51% of the monetary power that the network holds. This strongly disincentivizes attacking the network.
- With this algorithm, the entities put their cryptocurrency on the line as collateral.
- For more information on *PoS*, check out [this article](https://www.investopedia.com/terms/p/proof-stake-pos.asp).
</details>
</blockquote>
</details>
<details><summary>What 'puzzle' is the Proof of Work algorithm solving?</summary><br>

When a block (or collection of records),is 'mined' - meaning validated and added to the chain - a miner will have solved a very difficult mathematical puzzle to do so. With many puzzles, there is some bit of logic involved, however with bitcoin mining, the puzzle is completely random. Essentially the puzzle is solved by finding the nonce that, when added to the hash of the block itself, will produce a **new** hash with a predetermined number of leading zeros.

Solving the puzzle of which nonce will produce a new hash with **n** number of leading zeros is based solely on trial and error. Because of this it can be quite time intensive to decipher. Large quantities of electricity and computational power are used. This is why the winner of the nonce lottery receives a block reward for solving the puzzle and is the basis for the *Proof of Work* consensus algorithm.
</details>


<details><summary>What is the difference between a node and a miner?</summary><br>

Both miners and nodes are computers. A computer can serve as both miner and node - however, they perform different functions. A node is a computer that stores a copy of the blockchain. A miner is a computer that works to solve the puzzle that will allow a block of transactions to be validated and added to the network of nodes.

To learn about mining, click [this link](https://www.bitcoinmining.com/).

To learn more about nodes, click [this link](https://medium.com/coinmonks/blockchain-what-is-a-node-or-masternode-and-what-does-it-do-4d9a4200938f).

</details>

<details><summary>What is a digital Blockchain wallet?</summary><br>

A digital, or blockchain, wallet is simply an asymmetric keypair that acts as "keys" to your funds that are on the blockchain. It also serves as a place where you can view and send transactions.

Much like a debit card does not hold your actual money, but access to it, a blockchain wallet holds access to your funds but not the actual funds. The actual funds live on the blockchain.

For more reading on blockchain wallets, check out these articles from [investopedia](https://www.investopedia.com/terms/b/blockchain-wallet.asp) and [uncoin](https://blog.unocoin.com/what-happens-if-you-forget-your-bitcoin-wallet-keys-bbf563ce281a).

</details>

<details><summary>What is a Block explorer and how do I use it?</summary><br>

A block explorer is a tool that allows you to search transactions on a particular blockchain. Just as you might use a search engine to search topics online, the block explorer allows you to search blocks on the blockchain. With a block explorer, you can see various data about the block and drill down into the specifics. For example on Etherscan, a block explorer for Ethereum, you can find information such as:

* Block Height (block number on the chain)
* Transaction Hash
* From and To Address
* Entity that mined the block
* Block Reward
* Difficulty
* Gas

</details>

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
