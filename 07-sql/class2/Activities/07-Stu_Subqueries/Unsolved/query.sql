-- 1. Find the customer first and last names of those who have made payments.
SELECT first_name, last_name
from customer c
where customer_id in
	(
	select customer_id
	from payment p
	);

-- 2. Find the staff email addresses of those who have helped customers make payments.
select first_name, last_name, email
from staff s 
where staff_id in (
	select staff_id 
	from payment p 
	);

-- 3. Find the rental records of all films that have been rented out and paid for.
select *
from rental r 
where rental_id in (
	select rental_id 
	from payment p 
	);

-- BONUS
-- Something in csv data is causing error
drop table film;

CREATE TABLE film (
  film_id integer NOT NULL,
  title character varying(255) NOT NULL,
  description text,
  release_year integer,
  language_id smallint NOT NULL,
  original_language_id smallint,
  rental_duration smallint DEFAULT 3 NOT NULL,
  rental_rate numeric(4,2) DEFAULT 4.99 NOT NULL,
  length smallint,
  replacement_cost numeric(5,2) DEFAULT 19.99 NOT NULL,
  rating TEXT,
  last_update timestamp without time zone DEFAULT now() NOT NULL,
  special_features text[],
  fulltext tsvector NOT NULL
);
