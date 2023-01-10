SELECT * FROM employee_normalization;
SELECT * FROM first_nf_employee;
SELECT * FROM second_nf_employee;
SELECT * FROM second_nf_employee_email;
SELECT * FROM third_nf_employee;
SELECT * FROM third_nf_zipcode;

-- Bonus
SELECT *
FROM third_nf_employee AS a
LEFT JOIN second_nf_employee_email AS b ON a.employee_id = b.employee_id
LEFT JOIN third_nf_zipcode AS c ON a.zip_code = c.zip_code;
