select * from payment;

--1. What is the average payment amount?
select avg(amount) from payment; 

--2. What is the total payment amount?
select sum(amount) from payment;

--3. What is the minimum payment amount?
select min(amount) from payment; 

--4. What is the maximum payment amount?
select max(amount) from payment;

--5. How many customers has each staff serviced?
select staff_id, count(customer_id) from payment
group by staff_id;

--6. What is the count of payments for each customer?
select customer_id, count(payment_id) as "count_payments"
from payment
group by customer_id;

--7. Which customers have made over 40 payments?
select customer_id, count(payment_id) as count_payments
from payment
group by customer_id
having count(payment_id) > 40;