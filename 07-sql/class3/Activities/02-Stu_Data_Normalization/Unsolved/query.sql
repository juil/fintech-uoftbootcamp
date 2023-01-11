-- Import all data from csv
drop table employee_normalization;

select * from employee_normalization;

-- Create 1st Normalized Form
create table first_nf_employee
(like employee_normalization including all);

