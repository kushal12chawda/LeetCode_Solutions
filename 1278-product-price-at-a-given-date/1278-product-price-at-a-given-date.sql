/* Write your PL/SQL query statement below */
WITH RankedProducts AS (
    SELECT 
        product_id, 
        new_price,
        RANK() OVER (
            PARTITION BY product_id 
            ORDER BY change_date DESC
        ) AS rank
    FROM Products
    WHERE change_date <= DATE '2019-08-16'
)
SELECT 
    p.product_id, 
    COALESCE(rp.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN RankedProducts rp
ON p.product_id = rp.product_id AND rp.rank = 1;
