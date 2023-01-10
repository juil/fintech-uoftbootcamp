-- Query Tables
SELECT * FROM agents;
SELECT * FROM regions;
SELECT * FROM agent_region_junction;

-- A join statement to query all courses taken by students
SELECT *
FROM agents a
LEFT JOIN agent_region_junction b ON a.agent_id = b.agent_id
LEFT JOIN regions c ON b.region_id = c.region_id;