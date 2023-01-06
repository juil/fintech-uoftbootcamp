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