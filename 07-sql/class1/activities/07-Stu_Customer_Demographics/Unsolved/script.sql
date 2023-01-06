-- Drop existing table
drop table if exists customer;

-- Create table
create table customer (
	customer_id SERIAL primary key,
	first_name VARCHAR(30) not null,
	last_name varchar(30),
	gender varchar(30),
	age int,
	address varchar(50),
	city varchar(50),
	state char(2),
	zip_code char(6)
);

-- Copy data from CSV file
-- #TODO: Figure out user access permission for folder/file
copy customer from '/Users/juil/school/fintech-uoftbootcamp/classwork/07-sql/class1/activities/07-Stu_Customer_Demographics/Resources/customer.csv' with (FORMAT csv);

select * from customer;

-- Get all female customers
select first_name, last_name from customer
where gender = 'Female';

-- Query: male customers from New Jersey or Ohio
select first_name, last_name, state from customer
where gender = 'Male' and state = 'NJ' or state = 'OH';