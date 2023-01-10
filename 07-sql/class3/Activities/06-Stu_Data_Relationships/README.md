# Data Relationships

In this activity, you will implement a many-to-many relationship with the help of a junction table.

## Instructions

You are a database consultant at a national real estate firm. Your job is to design a database model for the real estate agents and their designated regions. The database will keep track of information on agents, regions in which the firm operates, and the regions each real estate agent is assigned.

* Begin by creating a new database named `agent_db`.

* Use the following CSV files to create and insert data for the `agents`, `regions`, and `agent_region_junction` tables:

  * [agents.csv](Resources/agents.csv)

  * [regions.csv](Resources/regions.csv)

  * [agent_region_junction.csv](Resources/agent_region_junction.csv)

* The `agent_region_junction` table should contain the following:

  * A foreign key relationship with the `agent_id` column in the `agents` table.

  * A foreign key relationship with the `region_id` column in the `regions` table.

  * A composite or multi-key primary key `agent_id` and `region_id`.

## Bonus

**Note:** Complete the bonus if time allows.

Join and query the tables to get all data on the agents.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
