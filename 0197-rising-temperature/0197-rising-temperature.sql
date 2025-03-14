SELECT Today.id
FROM Weather Today
INNER JOIN Weather Yesterday
ON (Today.recordDate - 1 = Yesterday.recordDate)
WHERE Today.temperature > Yesterday.temperature;
