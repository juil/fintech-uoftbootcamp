-- Query and return all data from customer table
SELECT *
FROM customer;

-- Query and return all female customers
SELECT *
FROM customer
WHERE gender = 'Female';

-- Query and return all male customers from New Jersey
select *
from customer
where gender = 'Male'
  AND state = 'NJ';

-- Query and return all male customers from New Jersey or Ohio
select *
from customer
where gender = 'Male'
  AND state = 'NJ' OR state = 'OH';

-- BONUS
-- Query and return all female customers from Maryland who are younger than 30 years old.
select *
from customer
where gender = 'Female'
  AND state = 'MD'
  AND age < 30;
