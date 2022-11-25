films=# select * from movies join actors on movies.id = actors.film_id;
 id |         name          | year | country | budget | id |     name     | film_id
----+-----------------------+------+---------+--------+----+--------------+---------
  1 | Baby Bulldog          | 2005 | USA     |   1000 |  1 | John Smith   |       1
  5 | Chain Reaction        | 2006 | USA     |   1000 |  2 | John Smith   |       5
 10 | French Twist          | 2005 | USA     |   1000 |  3 | John Smith   |      10
  1 | Baby Bulldog          | 2005 | USA     |   1000 |  4 | Andrew Stown |       1
  3 | Barbie: Mermaid Power | 2005 | USA     |   1000 |  5 | Andrew Stone |       3
 10 | French Twist          | 2005 | USA     |   1000 |  6 | Andrew Stone |      10
  1 | Baby Bulldog          | 2005 | USA     |   1000 |  7 | Scot Flaw    |       1
  3 | Barbie: Mermaid Power | 2005 | USA     |   1000 |  8 | Scot Flaw    |       3
  8 | Face of a Fugitive    | 2006 | USA     |   1000 |  9 | Scot Flaw    |       8
 10 | French Twist          | 2005 | USA     |   1000 | 10 | Scot Flow    |      10
  1 | Baby Bulldog          | 2005 | USA     |   1000 | 11 | Billy Johnes |       1
  3 | Barbie: Mermaid Power | 2005 | USA     |   1000 | 12 | Billy Johnes |       3

films=# select movies.name, year, country, budget, actors.name  from movies right join actors on movies.id = actors.film_id order by actors.name asc;
         name          | year | country | budget |     name
-----------------------+------+---------+--------+--------------
 French Twist          | 2005 | USA     |   1000 | Andrew Stone
 Barbie: Mermaid Power | 2005 | USA     |   1000 | Andrew Stone
 Baby Bulldog          | 2005 | USA     |   1000 | Andrew Stown
 Barbie: Mermaid Power | 2005 | USA     |   1000 | Billy Johnes
 Baby Bulldog          | 2005 | USA     |   1000 | Billy Johnes
 Baby Bulldog          | 2005 | USA     |   1000 | John Smith
 Chain Reaction        | 2006 | USA     |   1000 | John Smith
 French Twist          | 2005 | USA     |   1000 | John Smith
 Face of a Fugitive    | 2006 | USA     |   1000 | Scot Flaw
 Barbie: Mermaid Power | 2005 | USA     |   1000 | Scot Flaw
 Baby Bulldog          | 2005 | USA     |   1000 | Scot Flaw
 French Twist          | 2005 | USA     |   1000 | Scot Flow
(12 rows)

films=# select movies.name, year, country, budget, actors.name  from movies left join actors on movies.id = actors.film_id order by actors.name asc;
         name          | year | country | budget |     name
-----------------------+------+---------+--------+--------------
 French Twist          | 2005 | USA     |   1000 | Andrew Stone
 Barbie: Mermaid Power | 2005 | USA     |   1000 | Andrew Stone
 Baby Bulldog          | 2005 | USA     |   1000 | Andrew Stown
 Baby Bulldog          | 2005 | USA     |   1000 | Billy Johnes
 Barbie: Mermaid Power | 2005 | USA     |   1000 | Billy Johnes
 Chain Reaction        | 2006 | USA     |   1000 | John Smith
 Baby Bulldog          | 2005 | USA     |   1000 | John Smith
 French Twist          | 2005 | USA     |   1000 | John Smith
 Baby Bulldog          | 2005 | USA     |   1000 | Scot Flaw
 Barbie: Mermaid Power | 2005 | USA     |   1000 | Scot Flaw
 Face of a Fugitive    | 2006 | USA     |   1000 | Scot Flaw
 French Twist          | 2005 | USA     |   1000 | Scot Flow
 Getting Grace         | 2006 | USA     |   1000 |
 Here Out West         | 2008 | USA     |   1000 |
 Back to the Beach     | 2006 | Canada  |   1000 |
 Coming Apart          | 2008 | Canada  |   1000 |
 Camp Manna            | 2005 | USA     |   1000 |
 Final Justice         | 2005 | Spain   |   1000 |
 Dahmer                | 2005 | USA     |   1000 |
(19 rows)



