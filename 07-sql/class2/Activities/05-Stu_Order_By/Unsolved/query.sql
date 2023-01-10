-- Find the count of payments per customer in descending order
select customer_id, count(payment_id) as payment_count
from payment
group by customer_id
order by payment_count DESC;

-- Find the top 5 customers who have spend the most money
select customer_id, sum(amount) as amount_sum
from payment
group by customer_id 
order by amount_sum desc 
limit 5;


-- Find the bottom 5 customers who have spend the least money
select customer_id, sum(amount) as amount_sum
from payment
group by customer_id 
order by amount_sum asc 
limit 5;

-- Find the top 10 customers with the highest average payment
-- rounded to two decimal places
select customer_id, count(payment_id), sum(amount), avg(amount) as amount_avg
from payment
group by customer_id 
order by amount_avg desc 
limit 10;

-- BONUS 1 (Don't have staff table)
--SELECT first_name, last_name, COUNT(customer_id) AS customer_count
--FROM payment AS a
--JOIN staff AS b ON a.staff_id = b.staff_id
--GROUP BY first_name, last_name
--ORDER BY COUNT(customer_id) DESC;

-- BONUS 2
select cast(payment_date as DATE) as payment_date, count(*)
from payment 
group by cast(payment_date as DATE)
order by count(*) desc;


select column_name from information_schema.columns
where table_name = 'payment';

select * from payment;