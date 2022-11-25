films=# create table actors (id serial primary key, name varchar(30), film_id integer);

films=# insert into actors(name, film_id) values ('John Smith', 1), ('John Smith', 5), ('John Smith', 10), ('Andrew Stown', 1), ('Andrew Stone', 3), ('Andrew Stone', 10), ('Scot Flaw', 1), ('Scot Flaw', 3), ('Scot Flaw', 8), ('Scot Flow', 10), ('Billy Johnes', 1), ('Billy Johnes', 3);

films=# alter table movies add column country varchar(50) not null default 'USA';

films=# select * from movies where year>2005 and country = 'USA' order by year desc;
 id |        name        | year | country
----+--------------------+------+---------
 12 | Here Out West      | 2008 | USA
  5 | Chain Reaction     | 2006 | USA
  8 | Face of a Fugitive | 2006 | USA
 11 | Getting Grace      | 2006 | USA
(4 rows)

films=# select count(id) from movies where year>2005 and country = 'USA';
 count
-------
     4
(1 row)

films=# select max(year) from movies where year>2005 and country = 'USA';
 max
------
 2008
(1 row

films=# select * from movies where year between 2006 and 2007;
 id |        name        | year | country
----+--------------------+------+---------
  5 | Chain Reaction     | 2006 | USA
  8 | Face of a Fugitive | 2006 | USA
 11 | Getting Grace      | 2006 | USA
  2 | Back to the Beach  | 2006 | Canada
(4 rows)

films=# select * from movies where name ilike '%g%g%';
 id |     name      | year | country
----+---------------+------+---------
 11 | Getting Grace | 2006 | USA
(1 row)

films=# select * from movies where year in (2005, 2008);
 id |         name          | year | country
----+-----------------------+------+---------
  1 | Baby Bulldog          | 2005 | USA
  3 | Barbie: Mermaid Power | 2005 | USA
  4 | Camp Manna            | 2005 | USA
  7 | Dahmer                | 2005 | USA
 10 | French Twist          | 2005 | USA
 12 | Here Out West         | 2008 | USA
  6 | Coming Apart          | 2008 | Canada
  9 | Final Justice         | 2005 | Spain
(8 rows)


films=# select distinct year from movies;
 year
------
 2006
 2008
 2005
(3 rows)

films=# select count(distinct year) from movies;
 count
-------
     3
(1 row)

films=# alter table movies add column budget integer not null default 1000;
 id |         name          | year | country | budget
----+-----------------------+------+---------+--------
  1 | Baby Bulldog          | 2005 | USA     |   1000
  3 | Barbie: Mermaid Power | 2005 | USA     |   1000
  4 | Camp Manna            | 2005 | USA     |   1000
  5 | Chain Reaction        | 2006 | USA     |   1000
  7 | Dahmer                | 2005 | USA     |   1000
  8 | Face of a Fugitive    | 2006 | USA     |   1000
 10 | French Twist          | 2005 | USA     |   1000
 11 | Getting Grace         | 2006 | USA     |   1000
 12 | Here Out West         | 2008 | USA     |   1000
  2 | Back to the Beach     | 2006 | Canada  |   1000
  6 | Coming Apart          | 2008 | Canada  |   1000
  9 | Final Justice         | 2005 | Spain   |   1000
(12 rows)

films=# select country, year, sum(movies.budget) as "total budget" from movies group by country, year  order by country asc;
 country | year | total budget
---------+------+--------------
 Canada  | 2006 |         1000
 Canada  | 2008 |         1000
 Spain   | 2005 |         1000
 USA     | 2005 |         5000
 USA     | 2006 |         3000
 USA     | 2008 |         1000
(6 rows)

films=# select country, sum(budget) from movies group by movies.country;
 country | sum
---------+------
 Spain   | 1000
 USA     | 9000
 Canada  | 2000
(3 rows)



