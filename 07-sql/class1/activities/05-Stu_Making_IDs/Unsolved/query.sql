-- Schema
create table banks (
	bank_id SERIAL primary key,
	bank_name VARCHAR(50),
	bank_routing_number BIGINT
);

drop table banks;

-- Seed
-- Insert new data
INSERT INTO banks 
(bank_name, bank_routing_number)
VALUES
('Bank of America', 198491827),
('Wells Fargo', 629873495),
('JPMorgan Chase', 2340903984),
('Citigroup', 890123900),
('TD Bank', 905192010),
('Capital One', 184619239),
('Capital One', 184619239);

select * from banks

select * from banks 
where bank_name = 'Capital One';

delete from banks 
where bank_id = 7;

select * from banks;

-- Add banks
insert into banks 
	(bank_name, bank_routing_number)
values 
	('CIBC', 010),
	('TD Bank', 103);
	
select * from banks;

-- Change values
update banks
set bank_name = 'PNC Bank'
where bank_name = 'Citigroup';

select * from banks;

update banks 
set bank_routing_number = 1995826182
where bank_name = 'Wells Fargo';

select * from banks;

-- Add column to table with default value
alter table banks 
add mortgage_lending BOOLEAN default true;

select * from banks;


