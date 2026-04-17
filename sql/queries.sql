USE churn_project;

SELECT COUNT(*) FROM churn_simple;

SELECT Churn, COUNT(*) 
FROM churn_simple 
GROUP BY Churn;

SELECT Contract, Churn, COUNT(*) 
FROM churn_simple 
GROUP BY Contract, Churn;

SELECT 
  CASE 
    WHEN tenure <= 9 THEN '0-9'
    WHEN tenure <= 19 THEN '10-19'
    ELSE '>20'
  END AS tenure_group,
  Churn,
  COUNT(*)
FROM churn_simple
GROUP BY tenure_group, Churn;