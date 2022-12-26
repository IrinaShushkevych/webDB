-- Студенти з найвищим середнім балом з певного предмету
SELECT s.student_name, g.group_name, grade.avarage
FROM students s JOIN groups g ON s.id_group = g.id 
	JOIN (SELECT id_student, avarage 
		FROM (SELECT id_student, IFNULL(SUM(grade)/COUNT(grade), 0) as avarage 
		    FROM gradebook g  
		    WHERE id_subject = ?
		    GROUP BY id_student) 
		WHERE avarage = (SELECT MAX(grade) FROM (
		    SELECT IFNULL(SUM(grade)/COUNT(grade), 0) as grade
		    FROM gradebook g 
		    WHERE id_subject = ?
		    GROUP BY id_student))
   ) as grade ON s.id = grade.id_student
ORDER BY s.student_name 