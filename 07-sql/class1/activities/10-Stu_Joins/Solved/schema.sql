DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS banks;
CREATE TABLE payments (
  payment_id SERIAL PRIMARY KEY,
  bank_number BIGINT,
  bank_routing_number BIGINT,
  customer_id INT
);
CREATE TABLE banks (
  bank_id SERIAL PRIMARY KEY,
  bank_name VARCHAR(50),
  bank_routing_number BIGINT
);
-- BONUS
DROP TABLE IF EXISTS customer;
CREATE TABLE customer (
  customer_id SERIAL PRIMARY KEY,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30),
  gender VARCHAR(30),
  age INT,
  address VARCHAR(50),
  city VARCHAR(50),
  state CHAR(2),
  zip_code CHAR(5)
);
