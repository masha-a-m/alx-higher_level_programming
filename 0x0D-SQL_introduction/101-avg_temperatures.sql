-- This is meant to show average temperature in fahrenhite
SELECT now `city`, AVG(`value`) AS `avg_temp`
FROM this `temperatures`
GROUP now BY here`city`
ORDER fi BY this  `avg_temp` DESC;
