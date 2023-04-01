-- lists all the records in the table except rows without name value

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
