films=# 
SELECT actors.name as "actor", sum(budget) as "total budget"
FROM movies 
RIGHT JOIN actors
ON movies.id=film_id 
WHERE actors.name iLIKE '%john%' AND movies.year != 2006
GROUP BY actors.name;

    actor     | total budget
--------------+--------------
 Billy Johnes |         2000
 John Smith   |         2000
(2 rows)
