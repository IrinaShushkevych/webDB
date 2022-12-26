-- Оцінки студентів у певній групі з певного предмету на останньому занятті
SELECT g.createdAt, s.student_name, g.grade 
FROM students s LEFT JOIN  gradebook g ON s.id = g.id_student 
WHERE s.id_group = ? and
	  g.id_subject = ? AND 
	  g.createdAt  = (SELECT max(g.createdAt)
					FROM students s LEFT JOIN  gradebook g ON s.id = g.id_student 
					WHERE s.id_group = ? and g.id_subject = ?)