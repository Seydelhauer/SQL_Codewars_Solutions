/*Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions
Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.*/

-- my solution
SELECT (la_liga_goals + copa_del_rey_goals + champions_league_goals) AS res
FROM goals 