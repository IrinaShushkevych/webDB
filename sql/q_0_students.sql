SELECT g.id, g.group_name, s.id, s.student_name 
from students s LEFT JOIN groups g ON s.id_group = g.id 
GROUP BY g.group_name, s.student_name