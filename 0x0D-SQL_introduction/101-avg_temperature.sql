-- displays the average temperature by city
-- ordered by descending order of temperature

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
