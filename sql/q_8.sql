-- Середній бал, який ставив певний викладач зі своїх предметів
SELECT s.subject_name, IFNULL(SUM(grade)/COUNT(grade), 0) as avarage_grade
FROM subjects s LEFT JOIN gradebook g ON s.id = g.id_subject 
WHERE s.id_teacher = ?
GROUP BY s.subject_name 