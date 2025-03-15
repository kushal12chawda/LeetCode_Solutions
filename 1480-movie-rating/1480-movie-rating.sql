/* Write your PL/SQL query statement below */
(
  SELECT results FROM (
    SELECT Users.name AS results
    FROM MovieRating
    INNER JOIN Users ON MovieRating.user_id = Users.user_id
    GROUP BY Users.name
    ORDER BY COUNT(MovieRating.movie_id) DESC, Users.name
  ) WHERE ROWNUM = 1
)
UNION ALL
(
  SELECT results FROM (
    SELECT Movies.title AS results
    FROM MovieRating
    INNER JOIN Movies ON MovieRating.movie_id = Movies.movie_id
    WHERE TO_CHAR(MovieRating.created_at, 'YYYY-MM') = '2020-02'
    GROUP BY Movies.title
    ORDER BY AVG(MovieRating.rating) DESC, Movies.title
  ) WHERE ROWNUM = 1
);
