-- Список курсів, які певний викладач читає певному студенту
SELECT s.subject_name 
FROM  gradebook g LEFT JOIN subjects s ON g.id_subject = s.id 
WHERE g.id_student = ? and s.id_teacher = ?
GROUP BY s.subject_name 
ORDER BY s.subject_name 