-- Drop table "banks" if exists
DROP TABLE IF EXISTS banks;

-- Create new table
CREATE TABLE banks (
  bank_id SERIAL PRIMARY KEY,
  bank_name VARCHAR(50),
  bank_routing_number BIGINT
);