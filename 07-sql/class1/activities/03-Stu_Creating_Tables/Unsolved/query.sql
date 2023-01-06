CREATE TABLE states (
	state_name VARCHAR(50),
	state_abbreviation CHAR(2),
	population INT,
	state_property_tax_rate FLOAT
);

-- Insert data into the table
INSERT INTO states
(state_name, state_abbreviation, population, state_property_tax_rate)
VALUES
('Florida', 'FL', 21477737, 0.0093),
('Alabama', 'AL', 4903185, 0.0042),
('Texas', 'TX', 28995881, 0.0181),
('Kentucky', 'KY', 4467673, 0.0086),
('Virginia', 'VA', 8535519, 0.0081),
('Louisiana', 'LA', 4648794, 0.0053),
('Utah', 'UT', 3205958, 0.0064),
('Vermont', 'VT', 623989, 0.0188);


SELECT state_name FROM states;

select state_abbreviation, population, state_property_tax_rate from states
where population >5000000 and state_property_tax_rate < 0.01;

