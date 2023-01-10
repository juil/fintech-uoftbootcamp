DROP TABLE IF EXISTS owners CASCADE;
DROP TABLE IF EXISTS estates CASCADE;
DROP TABLE IF EXISTS estate_type CASCADE;
DROP TABLE IF EXISTS estates_new CASCADE;

-- Create owners table and insert values
CREATE TABLE owners (
  owner_id INT PRIMARY KEY NOT NULL,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

-- Create estates table and insert values
CREATE TABLE estates (
  estate_id INT NOT NULL PRIMARY KEY,
  owner_id INT NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES owners(owner_id),
  address VARCHAR(255),
  city VARCHAR (255),
  state VARCHAR(255),
  zip_code VARCHAR(255)
);

-- BONUS
-- Create estate_type table and insert data
CREATE TABLE estate_type (
  estate_type_id INT NOT NULL PRIMARY KEY,
  estate_type VARCHAR(255)
);

-- Create new estates table and insert values
CREATE TABLE estates_new (
  estate_id INT NOT NULL PRIMARY KEY,
  owner_id INT NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES owners(owner_id),
  address VARCHAR(255),
  city VARCHAR (255),
  state VARCHAR(255),
  zip_code VARCHAR(255),
  estate_type_id INT,
  FOREIGN KEY (estate_type_id) REFERENCES estate_type(estate_type_id)
);

