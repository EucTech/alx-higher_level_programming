-- a script that creates a table second_table
-- insert values to it

CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table VALUES (id, name, score)
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bod", 14),
	(4, "George", 8);
