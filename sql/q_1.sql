-- 5 студентів з найбільшим середнім балом з усіх предметів
SELECT s.student_name, gr.group_name, IFNULL(SUM(g.grade)/COUNT(g.grade), 0) as avarage_grade 
FROM  students s LEFT JOIN groups gr ON s.id_group = gr.id 
	LEFT JOIN gradebook g ON s.id = g.id_student 
group by g.id_student 
order by avarage_grade DESC, s.student_name 
LIMIT 5