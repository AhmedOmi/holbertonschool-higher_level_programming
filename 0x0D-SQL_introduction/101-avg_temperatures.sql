-- script select avg-tmp from temperature table
SELECT city, AVG(value) AS "avg_temp" FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
