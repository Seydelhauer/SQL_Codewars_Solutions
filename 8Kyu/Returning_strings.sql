/*Write a select statement that takes name from person table and return "Hello, <name> how are you doing today?" results in a column named greeting
*/

-- my solution
select CONCAT('Hello, ', name, ' how are you doing today?') as greeting from person