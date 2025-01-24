/*Given a demographics table in the following format:

** demographics table schema **

id
name
birthday
race
you need to return the same table where all text fields (name & race) are changed to the bit length of the string.*/
-- my solution
SELECT id,
  LENGTH(name) * 8 as name,
  birthday,
  LENGTH(race) * 8 as race
FROM demographics;