/*
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
*/

-- my solution

Select number,
  Case When number%2=0 then number*8
  else number*9
  end as res
from multiplication