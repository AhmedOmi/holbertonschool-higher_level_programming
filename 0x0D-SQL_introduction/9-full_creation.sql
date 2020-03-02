-- creates a table second_table in the database
-- script sql
CREATE TABLE IF NOT EXIST second_table(
id INT,
name VARCHAR(256),
score INT);
-- insert in new table	
INSERT INTO second_table (id, name, score)
VALUES(1, 'John', 10),
      (2,'Alex',3),
      (3,'Bob', 14),
      (4,'George', 8);
