-- Insert Data into table
INSERT INTO agents (agent_id, first_name, last_name)
VALUES
  (1, 'Diana', 'Lee'),
  (2, 'Anthony', 'Garcia'),
  (3, 'Karen', 'Clinton');

INSERT INTO regions (region_id, region_name)
VALUES
  (11, 'Northeast'),
  (22, 'South'),
  (33, 'Midwest'),
  (44, 'West');

INSERT INTO agent_region_junction (agent_id, region_id)
VALUES
  (1,11),
  (1,33),
  (2,44),
  (2,33),
  (3,22),
  (3,33),
  (3,44);