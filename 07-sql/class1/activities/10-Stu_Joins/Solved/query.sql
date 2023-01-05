-- Perform an INNER JOIN
select
  *
from payments as a
INNER JOIN banks as b ON a.bank_routing_number = b.bank_routing_number;
-- Perform a LEFT JOIN
select
  *
from payments as a
LEFT JOIN banks as b ON a.bank_routing_number = b.bank_routing_number;
-- Perform a RIGHT JOIN
select
  *
from payments as a
RIGHT JOIN banks as b ON a.bank_routing_number = b.bank_routing_number;
-- Perform a FULL OUTER JOIN
select
  *
from payments as a FULL
OUTER JOIN banks as b ON a.bank_routing_number = b.bank_routing_number;
-- Perform a CROSS JOIN
select
  *
from payments
CROSS JOIN banks;
-- BONUS
select
  a.payment_id,
  a.bank_number,
  a.bank_routing_number,
  b.bank_name,
  c.first_name,
  c.last_name
from payments as a
INNER JOIN banks as b ON a.bank_routing_number = b.bank_routing_number
INNER JOIN customer as c ON a.customer_id = c.customer_id;
