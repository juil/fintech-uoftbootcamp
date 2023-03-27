# Peoplechain

In this activity, you will work with a group to emulate the basic functioning of a blockchain by creating a distributed-ledger-like system.

Specifically, your group will act as the following:

* A blockchain user, sending and receiving cryptocurrency.

* A blockchain node with responsibilities for validating transactions.

* A blockchain miner with responsibilities for writing blocks to the chain.

## Activity Preparation

Before beginning the activity, be sure to do the following:

1. Subscribe to the following four channels in your class’s group Slack:

    * Balance
    * Broadcasted Transactions
    * MemPool
    * Blockchain

2. With your group, choose a team name that corresponds to the first name of one of the students in the group (for example, Group Tom or Group Adriana).

## Instructions

The activity is divided into four steps.

1. Post cryptocurrency balances on the blockchain.

2. Create blockchain transactions.

3. Validate blockchain transactions.

4. Mine blockchain transactions.

You must complete each step before you can proceed to the next step.

### 1. Post Cryptocurrency Balances on the Blockchain

Post a cryptocurrency account balance in the Balance channel in Slack. The message should be sent by the individual that the group is named after. For example, Adriana should post the balance for Group Adriana. It should be posted in the following format:

  ```text
  Group Tom: 10 BTC
  ```

### 2. Create a Blockchain Transaction

Now, your group will act as a Bitcoin user. Each group member (the group namesake) who posted in the Balance channel in Step 1 will now post one transaction in the following format to the Broadcasted Transactions channel:

  ```text
  to: Group Adriana, from: Group Tom, amount: 3 BTC, fee: .01 BTC
  ```

Every transaction, no matter the size, should include a fee of .01 BTC.

> **Note:** Your group is not required to post a valid transaction. For example, you can send more BTC than you have (according to the balance you posted in Step 1), or send BTC to your own group from another group. Transactions will be validated in the next step.

### 3. Validate Blockchain Transactions

In this step, your group will act as a node in the blockchain network by validating the transactions.

In this activity, a transaction is **valid** if it meets the following conditions:

* The group name in the “from” section (see the transaction format in Step 2) matches the name of the sender in the Slack message. Think of this as a digital signature.

* The amount sent is not larger than the group’s balance.

To validate a transaction:

* One person from your group should give it a “thumbs up” in the Broadcasted Transactions channel.

Once a transaction has received a “thumbs up” from at least half of the groups in the class, a member of the instructional staff will copy the transaction from the “Broadcasted Transactions” channel and paste it in the “MemPool” channel.

* **Hint:** In a blockchain network, a mempool contains validated transactions that are waiting to be confirmed.

### 4. Mine Blockchain Transactions

In this final step, you will act as a miner on the blockchain.

Your instructor will choose a random number between 1 and 10. Your group will post its guess in the Class Activities channel.

The group that guesses correctly first gets to add five transactions to the next block in the Blockchain channel. To do so, one of your group members will create a “block” message in the channel. In this case, a “block” should look like the following code snippet:

  ```text
  Previous block hash - 0
  to: Group Adriana, from: Group Tom, amount: 3 BTC, fee: .01 BTC
  to: Group Tom, from: Group Adriana, amount: 1.33333 BTC, fee: .01 BTC
  to: Group Arturo, from: Group Aubrey, amount: 7 BTC, fee: .01 BTC
  to: Group Jose, from: Group Nikhel, amount: 1.25 BTC, fee: .01 BTC
  to: Group Samson, from: Group Tanisha, amount:  2.7594 BTC, fee: .01 BTC
  Current block hash - 1
  ```

For this task, be aware of the following:

* The transactions can be copied and pasted from the MemPool channel. Once a transaction is “mined,” it should be marked in MemPool with a checkmark so that it’s not duplicated on the blockchain by other miners.

* For the first block that’s mined, the previous block hash is 0, and the current block hash is 1. For the second block that’s mined, the previous block hash is 1, and the current block hash is 2. The hash count progresses until all transactions have been mined in blocks.

* The mining group will receive a reward of 1 BTC as well as the sum of all transaction fees for the transactions added to the pool, for a total of 1.05 BTC to add to their cryptocurrency balance.

Repeat Step 4 until all transactions from the MemPool channel are added to the chain.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
