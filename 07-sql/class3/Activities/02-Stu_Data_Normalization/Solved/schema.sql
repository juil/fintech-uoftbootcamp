DROP TABLE IF EXISTS employee_normalization;
DROP TABLE IF EXISTS first_nf_employee;
DROP TABLE IF EXISTS second_nf_employee;
DROP TABLE IF EXISTS second_nf_employee_email;
DROP TABLE IF EXISTS third_nf_employee;
DROP TABLE IF EXISTS third_nf_zipcode;

CREATE TABLE employee_normalization (
	employee_id INT,
	name VARCHAR(255),
	age INT,
	address VARCHAR(255),
	city VARCHAR(255),
	state VARCHAR(255),
	zip_code INT,
	email VARCHAR(255)
);

CREATE TABLE first_nf_employee
(
	employee_id INT,
	name VARCHAR(255),
	age INT,
	address VARCHAR(255),
	city VARCHAR(255),
	state VARCHAR(255),
	zip_code INT,
	email VARCHAR(255)
);

CREATE TABLE second_nf_employee
(
	employee_id INT PRIMARY KEY,
	name VARCHAR(255),
	age INT,
	address VARCHAR(255),
	city VARCHAR(255),
	state VARCHAR(255),
	zip_code INT
);

CREATE TABLE second_nf_employee_email
(
	email_id INT PRIMARY KEY,
	employee_id INT,
	email VARCHAR(255)
);

CREATE TABLE third_nf_employee
(
	employee_id INT PRIMARY KEY,
	name VARCHAR(255),
	age INT,
	address VARCHAR(255),
	zip_code INT
);

CREATE TABLE third_nf_zipcode
(
	zip_code INT PRIMARY KEY,
	city VARCHAR(255),
	state VARCHAR(255)
);
