-- View the table data
SELECT *
FROM states;

-- Use a query to view only the state name
SELECT state_name
FROM states;

-- Bonus 1:
-- Create a query to view only state abbreviations
SELECT state_abbreviation
FROM states;

-- Bonus 2:
-- Create a query to view states
-- with a population greater than 5,000,000
SELECT *
FROM states
WHERE population > 5000000;

-- Bonus 3:
-- Create a query to view states
-- with a population of greater than 5,000,000
-- and a state property tax rate of less than 0.01
SELECT *
FROM states
WHERE population > 5000000
AND state_property_tax_rate < 0.01;
