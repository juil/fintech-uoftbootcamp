-- sales_db
-- Create table
-- Drop table if exists
DROP TABLE IF EXISTS sales;

-- Create new table to import data
CREATE TABLE sales (
  sales_id SERIAL PRIMARY KEY,
  payment_id INT,
  mortgage_id INT,
  loan_amount INT,
  loan_date DATE
);

-- Return records with loan amounts less than $300,000
select sales_id, loan_amount from sales
where loan_amount > 300000;

-- Find the average loan amount of all sales records
select avg(loan_amount) from sales;