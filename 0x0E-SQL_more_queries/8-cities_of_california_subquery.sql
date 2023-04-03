-- lists all te cities of California that is in the database

SELECT id, name FROM cities WHERE state_id = (SELECT if FROM states WHERE name = "California") ORDER BY id;
