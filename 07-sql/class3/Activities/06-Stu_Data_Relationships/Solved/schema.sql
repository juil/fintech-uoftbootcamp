-- Drop tables
DROP TABLE IF EXISTS agents CASCADE;
DROP TABLE IF EXISTS regions CASCADE;
DROP TABLE IF EXISTS agent_region_junction CASCADE;

-- Create a table of students
CREATE TABLE agents (
  agent_id INT PRIMARY KEY,
  first_name VARCHAR NOT NULL,
  last_name VARCHAR NOT NULL
);

-- Create a table of courses
CREATE TABLE regions (
  region_id INT NOT NULL PRIMARY KEY,
  region_name VARCHAR NOT NULL
);

-- Create a junction table.
CREATE TABLE agent_region_junction (
  agent_id INT NOT NULL,
  FOREIGN KEY (agent_id) REFERENCES agents(agent_id),
  region_id INTEGER NOT NULL,
  FOREIGN KEY (region_id) REFERENCES regions(region_id),
  PRIMARY KEY (agent_id, region_id)
);
