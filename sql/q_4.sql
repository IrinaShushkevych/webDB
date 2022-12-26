-- Середній бал на потоці (по всіх)
SELECT IFNULL(SUM(grade)/COUNT(grade), 0) as avarage
FROM gradebook