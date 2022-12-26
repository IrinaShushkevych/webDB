-- Середній бал у групах з певнjого предмету
SELECT group_name, IFNULL(SUM(grade)/COUNT(grade), 0) as avarage 
FROM (
	SELECT id_student, grade
	FROM gradebook 
	WHERE id_subject = ?) as grade LEFT JOIN (
        SELECT s2.id, s2.student_name, g2.group_name 
        FROM students s2 JOIN groups g2 ON s2.id_group = g2.id 
        ) as stud ON grade.id_student = stud.id
GROUP BY group_name