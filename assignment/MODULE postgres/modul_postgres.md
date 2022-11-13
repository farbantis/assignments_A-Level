[//]: # (1)
postgres=# CREATE TABLE module_1 (id serial primary key, name varchar(20), pwd varchar(50), email varchar(50), genger varchar(1));
CREATE TABLE
postgres=# table module_1;
 id | name | pwd | email | genger
----+------+-----+-------+--------
(0 rows)

postgres=# ALTER TABLE module_1 RENAME COLUMN genger TO gender;
ALTER TABLE
postgres=# table module_1;
 id | name | pwd | email | gender
----+------+-----+-------+--------
(0 rows)

postgres=# INSERT INTO module_1 (name, pwd, email, gender) VALUES('Vasya', '21341234qwfsdf', 'mmm@mmail.com', 'm'), ('Alex', '21341234', 'mmm@gmail.com', 'm'), ('Alexey', 'qq21341234Q', 'alexey@gmail.com', 'm'), ('Helen', 'MarryMeeee', 'hell@gmail.com', 'f'), ('Jenny', 'SmakeMyb', 'eachup@gmail.com', 'f'), ('Lora', 'burn23', 'tpicks@gmail.com', 'f');
INSERT 0 6
postgres=# table module_1;
 id |  name  |      pwd       |      email       | gender
----+--------+----------------+------------------+--------
  1 | Vasya  | 21341234qwfsdf | mmm@mmail.com    | m
  2 | Alex   | 21341234       | mmm@gmail.com    | m
  3 | Alexey | qq21341234Q    | alexey@gmail.com | m
  4 | Helen  | MarryMeeee     | hell@gmail.com   | f
  5 | Jenny  | SmakeMyb       | eachup@gmail.com | f
  6 | Lora   | burn23         | tpicks@gmail.com | f
(6 rows)

[//]: # (2)
postgres=# 
SELECT 
  CONCAT('This is ',name, ' ', 
        CASE 
          WHEN gender='f' THEN 'she' 
          ELSE 'he' 
        END, 
         ' has email ', email) 
  AS info 
FROM module_1;

                     info
----------------------------------------------
 This is Vasya he has email mmm@mmail.com
 This is Alex he has email mmm@gmail.com
 This is Alexey he has email alexey@gmail.com
 This is Helen she has email hell@gmail.com
 This is Jenny she has email eachup@gmail.com
 This is Lora she has email tpicks@gmail.com
(6 rows)

[//]: # (3)
postgres=# 
SELECT 
  CONCAT('We have ', 
    count(id), ' ', 
    CASE 
      WHEN gender='m' THEN 'boys' 
      WHEN gender='f' THEN 'girls'
    END, '!')
  AS "Gender information"
FROM module_1 group by gender;


 Gender information
--------------------
 We have 3 boys!
 We have 3 girls!
(2 rows)

[//]: # (4)

[//]: # (5)

postgres=# \timing
Timing is on.
postgres=# 
SELECT
  vocabulary.name,
  COUNT(vocabulary.id) AS words
FROM vocabulary
  LEFT JOIN word 
  ON vocabulary.id=vocabulary_id 
GROUP BY vocabulary.name;

  name   | words
---------+-------
 animals |    10
 school  |    10
 SF      |    10
 human   |    10
 nature  |    10
(5 rows)


Time: 0,852 ms
postgres=#