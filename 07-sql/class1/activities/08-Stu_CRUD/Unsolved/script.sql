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

-- Load table data 
copy sales from '/Users/juil/school/fintech-uoftbootcamp/classwork/07-sql/class1/activities/08-Stu_CRUD/Resources/sales.csv' with (FORMAT csv);

select * from sales;

-- Return records with loan amounts less than $300,000
select sales_id, loan_amount from sales
where loan_amount > 300000;

-- Find the average loan amount of all sales records
select avg(loan_amount) from sales;

-- Update sales_id 33
select sales_id, loan_amount from sales
where sales_id = 33;

update sales 
set loan_amount = 423212
where sales_id = 33;

-- Add new boolean column loan_distributed with default: True
alter table sales
add column loan_distributed BOOLEAN default true;

-- Insert new record
insert into sales 
(sales_id, payment_id, mortgage_id, loan_amount, loan_date)
values (101, 101, 2, 734544, '1995-10-05');

select * from sales
where sales_id = 101;

-- Delete data
delete from sales 
where sales_id = 72;

select * from sales 
where sales_id = 72;