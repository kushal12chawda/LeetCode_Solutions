/* Write your PL/SQL query statement below */
WITH CustomerToIsImmediate AS (
    SELECT DISTINCT customer_id,
           FIRST_VALUE(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) OVER (PARTITION BY customer_id 
    ORDER BY order_date) AS is_immediate
    FROM Delivery
)
SELECT ROUND(AVG(is_immediate) * 100, 2) AS immediate_percentage
FROM CustomerToIsImmediate;
