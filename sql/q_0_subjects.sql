SELECT s.id, s.subject_name, t.id, t.teacher_name  
FROM subjects s LEFT JOIN teachers t ON s.id_teacher = t.id  