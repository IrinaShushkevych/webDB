-- Оцінки студентів у окремій группі з певного предмету
SELECT g.createdAt  as grade_date, s.student_name, g.grade
FROM students s LEFT JOIN gradebook g ON s.id = g.id_student
WHERE s.id_group = ? and g.id_subject = ?
ORDER BY g.createdAt , s.student_name