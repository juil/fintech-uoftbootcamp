SELECT * FROM owners;
SELECT * FROM estates;

-- Attempt to insert data without referential integrity
INSERT INTO estates
(estate_id, owner_id, address, city, state, zip_code)
VALUES
(9, 10, '23 Delafield Avenue', 'New Brunswick', 'NJ', 08901);

-- Insert new record into owner table
INSERT INTO owners
(owner_id, first_name, last_name)
VALUES
(10, 'David', 'Stone');

-- Re-attempt to insert data with referential integrity
INSERT INTO estates
(estate_id, owner_id, address, city, state, zip_code)
VALUES
(9, 10, '23 Delafield Avenue', 'New Brunswick', 'NJ', 08901);

-- Select all columns from joined table
SELECT *
FROM owners
INNER JOIN estates ON owners.owner_id = estates.owner_id;

-- select explicit columns from joined table
SELECT
  owners.first_name,
  owners.last_name,
  estates.address,
  estates.city,
  estates.state,
  estates.zip_code
FROM owners
INNER JOIN estates ON owners.owner_id = estates.owner_id;

-- BONUS
SELECT * FROM estate_type;
SELECT * FROM estates_new;

-- Join all three tables
SELECT *
FROM owners
INNER JOIN estates_new ON owners.owner_id = estates_new.owner_id
INNER JOIN estate_type ON estates_new.estate_type_id = estate_type.estate_type_id;
