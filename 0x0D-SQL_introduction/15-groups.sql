-- lists the number of records having the same score

SELECT score, COUNT(*) AS number FROM second_table GROUP_BY score ORDER BY number DESC;
