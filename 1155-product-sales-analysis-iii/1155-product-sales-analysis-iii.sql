/* Write your PL/SQL query statement below */
WITH ProductToYear AS (
    SELECT product_id, MIN(year) AS year
    FROM Sales
    GROUP BY product_id
)
SELECT Sales.product_id, ProductToYear.year AS first_year, Sales.quantity, Sales.price
FROM Sales
INNER JOIN ProductToYear
ON Sales.product_id = ProductToYear.product_id 
AND Sales.year = ProductToYear.year;
