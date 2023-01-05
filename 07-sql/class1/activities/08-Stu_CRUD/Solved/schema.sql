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
