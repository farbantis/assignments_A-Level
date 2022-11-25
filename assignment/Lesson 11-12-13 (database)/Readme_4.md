films=# create table sample_list (id serial primary key, product varchar(50), price integer);
CREATE TABLE
films=# table sample_list
films-# ;
 id | product | price
----+---------+-------
(0 rows)


films=# insert into sample_list(product, price) values('phone', 100), ('shirt', 20), ('shoes', 12), ('car', 3000), ('truck', 5000);
INSERT 0 5
films=# table sample_list;
 id | product | price
----+---------+-------
  1 | phone   |   100
  2 | shirt   |    20
  3 | shoes   |    12
  4 | car     |  3000
  5 | truck   |  5000
(5 rows)


films=# update sample_list set price = price * 1.2 where price < 50;
UPDATE 2
films=# table sample_list;
 id | product | price
----+---------+-------
  1 | phone   |   100
  4 | car     |  3000
  5 | truck   |  5000
  2 | shirt   |    24
  3 | shoes   |    14
(5 rows)


films=# delete from sample_list where price <15 or product ='phone';
DELETE 2
films=# table sample_list;
 id | product | price
----+---------+-------
  4 | car     |  3000
  5 | truck   |  5000
  2 | shirt   |    24
(3 rows)


films=#