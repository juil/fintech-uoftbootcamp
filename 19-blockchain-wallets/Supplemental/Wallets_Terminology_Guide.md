# Blockchain Terminology Guide

This guide serves as an overview for the various concepts required to understand the fundamentals of blockchain networks.

## Terminologies

* What is a blockchain?

  **Answer:** A blockchain is a network of nodes or machines linked in a peer-to-peer fashion that facilitates transactions in a verifiable and permanent way. A blockchain network is also often called an open distributed ledger.

* What is a blockchain node?

  **Answer:** A node is a single machine that contributes to the infrastructure of a blockchain network. Blockchains networks, as a whole, are composed of multiple nodes that are interconnected with each other. Nodes exchange the latest blockchain data with each other so that each node is up-to-date with the latest verified transactions on the blockchain network.

* What is blockchain mining?

  **Answer:** Blockchain mining is the process of adding verified transaction records to the current blockchain data. Miners act as separate nodes that are paid a fee to verify blockchain transactions, and do so by solving intense computations to finalize transactions.

* What is a blockchain wallet?

  **Answer:** A blockchain wallet is a digital wallet containing a public and private key that is used to not only store cryptocurrencies, but also conduct secure transactions amongst other users via wallet addresses (hashed version of a public key). It is imperative that the private key for a digital wallet be kept safe, as losing it will prevent a user from accessing their funds (no other way for decryption).

* What is Ethereum?

  **Answer:** Ethereum is an open software platform based on blockchain technology that enables developers to build and deploy decentralized applications.

* What is a hash?

  **Answer:** A hash value is a product of a function that converts an input of letters and numbers into an encrypted output of a fixed length. Hashing is one way to enable security during message transmission when it is intended for a particular recipient only. This helps ensure that the message is not tampered with, as doing so would generate a new hash value different from the original hash value.

* What is a digital signature?

  **Answer:** A digital signature is a numerical value that is represented as a sequence of characters. It is the product of ensuring the contents of a message have not been altered in transit (integrity), that the message was indeed sent by the sender (authentication), and that the sender cannot deny having sent the message (non-repudiation).

* What is encryption?

  **Answer:** Encryption is the process in which a message is encoded in a format that cannot be read or understood by an external party lacking the necessary credentials.

* What is symmetric encryption?

  **Answer:** Symmetric encryption is the simplest type of encryption that uses only a single key (a private/secret key) to both encrypt and decrypt information. As a result, the parties communicating via symmetric encryption must exchange the secret key so that it can be used in the decryption process, which is a security disadvantage compared to asymmetric encryption.

* What is an asymmetric key?

  **Answer:** Asymmetric encryption uses a key pair: a public and private key. As the name suggests, the public key is made freely available to anyone on the internet, while the private key is kept a secret by the end-user. Therefore, messages that are encrypted using the public key can only be decrypted using the associated private key, and messages that are encrypted using the private key can only be decrypted using the associated public key.

* What are the advantages vs. disadvantages of both types of encryption techniques?

  **Answer:** Symmetric encryption is the oldest and best-known technique for encryption. However, because of its use of a single key (the private/secret key), there is the potential for a security breach when exchanging the private key between two parties, especially over a vast network such as the internet with possible eavesdroppers. In contrast, due to the use of a key pair in asymmetric encryption (public and private key), the private key is never exchanged, and therefore is kept secret at all times. Using  a key pair does result in asymmetric encryption being slower than symmetric encryption, due to the increased processing power used to encrypt and decrypt messages.

* What is a consensus algorithm?

  **Answer:** A consensus algorithm is a protocol used to verify the validity of transactions on a blockchain network. Due to the decentralized nature of the blockchain network, there is no central authority, and therefore nodes within the blockchain network must be able to verify such transactions with certainty.

* What is proof of authority?

  **Answer:** Proof of Authority (PoA) is a reputation-based consensus algorithm in which the model relies on a limited number of block validators that act as moderators to verify the newest blocks and transactions.

* What is proof of work?

  **Answer:** Proof of Work (PoW) is an asset-based consensus algorithm in which the model relies on producing a piece of data which is both resource (computation) and time intensive, but allows for others to verify the validity of the transaction. This consensus algorithm directly relates to the blockchain mining concept, in which miners solve intense computations to finalize transactions.

* What is proof of stake?

  **Answer:** Proof of Stake (PoS) is a collateral-based consensus algorithm in which the model relies on transactional validators who are selected based on the amount of Bitcoin or Ether they hold. When they validate transactions, they put up a stake of their own Bitcoin or Ether and are rewarded (proportional to their stake) when a new block or transaction is added to the blockchain.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
