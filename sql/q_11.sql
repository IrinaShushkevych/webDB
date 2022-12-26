-- Середній бал, який певний викладач ставить певному студенту
SELECT IFNULL(SUM(g.grade)/COUNT(g.grade), 0) as avarage
FROM gradebook g LEFT JOIN subjects s ON g.id_subject = s.id 
WHERE g.id_student = ? and s.id_teacher = ?