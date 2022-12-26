import sqlite3
import faker
import os
from random import randint
from datetime import datetime, timedelta

qparams = [
    [0, 0],
    [1, 2],
    [1, 1],
    [0, 0],
    [1, 1],
    [1, 1],
    [2, 1],
    [1, 1],
    [1, 1],
    [2, 1],
    [2, 1],
    [2, 2]
    ]

class Univer:
    def __init__(self, db = None):
        if not db:
            self.db = os.path.join('db', 'web06.db')
        else:
            self.db = db
        self.conn = None

    def create_table(self):
        with open(os.path.join('sql', 'create_table.sql'), 'r') as f:
            sql = f.read()

        cur = self.conn.cursor()
        cur.executescript(sql)
        cur.close()
        self.conn.commit()

    def create_data_DB(self):
        count_group = 3
        count_student = 50
        count_teacher = 5
        count_subject = 8
        count_grade = 20
        count_subject_group = 4
        fake = faker.Faker()

        students = [(fake.name(), randint(1, count_group)) for _ in range(count_student)]
        teachers = [(fake.name(), ) for _ in range(count_teacher)]
        subjects = [(f'Subject_{i + 1}', randint(1, count_teacher)) for i in range(count_subject)]
        groups = [(f'G_{i + 1}', ) for i in range(count_group)]

        grades = []
        d_now = datetime.now()
        group_subject = []
        for i in range(count_group):
            gs = set()
            while len(gs) < count_subject_group:
                gs.add(randint(1, count_subject))
            group_subject.append((i + 1, list(gs)))
        for i in range(len(students)):
            
            for delta in range(count_grade):
                d = (d_now - timedelta(delta)).strftime('%Y-%m-%d')
                sub = randint(0, len(group_subject[students[i][1] - 1][1]) - 1)
                grades.append((i + 1, group_subject[students[i][1] - 1][1][sub], randint(3,5), d))

        return {
            'students': students,
            'teachers': teachers,
            'subjects': subjects,
            'groups': groups,
            'grades': grades
        }

    def fill_DB(self):
        data = self.create_data_DB()
        cur = self.conn.cursor()

        # fill table groups
        sql = '''
            INSERT INTO groups (group_name)  VALUES (?)
        '''
        cur.executemany(sql, data['groups'])
        
        # fill table students
        sql = '''
            INSERT INTO students (student_name, id_group)  VALUES (?, ?)
        '''
        cur.executemany(sql, data['students'])

        # fill table teachers
        sql = '''
            INSERT INTO teachers (teacher_name)  VALUES (?)
        '''
        cur.executemany(sql, data['teachers'])

        #fill table subjects
        sql = '''
            INSERT INTO subjects (subject_name, id_teacher)  VALUES (?, ?)
        '''
        cur.executemany(sql, data['subjects'])

        #fill table gradebook
        sql = '''
            INSERT INTO gradebook (id_student, id_subject, grade, createdAt)  VALUES (?, ?, ?, ?)
        '''
        cur.executemany(sql, data['grades'])

        cur.close()
        self.conn.commit()

    def info_from_db(self):
        cur = self.conn.cursor()
        path_query = os.path.join('sql', 'q_0_subjects.sql')
        if not os.path.exists(path_query):
            return 'Wrong number of query!'
        with open(path_query, 'r') as f:
            sql = f.read()
        cur.execute(sql)
        subjects = cur.fetchall()
        print('-----------------------------------------------')
        print(' Subject - Teachers')
        print('-----------------------------------------------')
        for el in subjects:
            print(el[0], el[1], ' - ', el[2], el[3])
        print('-----------------------------------------------')

        path_query = os.path.join('sql', 'q_0_students.sql')
        if not os.path.exists(path_query):
            return 'Wrong number of query!'
        with open(path_query, 'r') as f:
            sql = f.read()
        cur.execute(sql)
        students = cur.fetchall()
        print('-----------------------------------------------')
        print(' Group - Students')
        print('-----------------------------------------------')
        for el in students:
            print(el[0], el[1], ' - ', el[2], el[3])
        print('-----------------------------------------------')        

        cur.close()
        return (subjects, students)
        
    def query(self, num = None, *args):
        num = int(num)
        if num == 0:
            return self.info_from_db()
        if not num:
            return 'Send number of query!'
        path_query = os.path.join('sql', f'q_{num}.sql')
        if not os.path.exists(path_query):
            return 'Wrong number of query!'
        with open(path_query, 'r') as f:
            sql = f.read()

        cur = self.conn.cursor()
        if len(args) != qparams[num - 1][0]:
            return 'Wrong count of params'
        if args:
            param = []
            for _ in range(qparams[num - 1][1]):
                param += args
            cur.execute(sql, (*param,))
        else:
            cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        self.print_result(result)
        return result

    def print_result(self, result):
        for el in result:
            printstr = []
            for i in range(len(el)):
                printstr.append(el[i])
            print(*printstr, sep='   |   ')

    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        return self

    def __exit__(self, type, value, traceback):
        self.conn.close()
        self.conn = None

    def print_help(self):
        print(' 0) Інформація про студентів, викладачів та предмети')
        print(' 1) 5 студентів з найбільшим середнім балом з усіх предметів')
        print(' 2) Студенти з найвищим середнім балом з певного предмету (параметри: id предмету)')
        print(' 3) Середній бал у групах з певного предмету (параметри: id предмету)')
        print(' 4) Середній бал на потоці (по всіх)')
        print(' 5) Курси певного викладача (параметри: id викладача)')
        print(' 6) Список студентів певної групи (параметри: id групи)')
        print(' 7) Оцінки студентів у окремій группі з певного предмету (параметри: id предмету, id групи)')
        print(' 8) Середній бал, який ставив певний викладач зі своїх предметів (параметри: id викладача)')
        print(' 9) Список курсів, які відвідував студент (параметри: id студента)')
        print(' 10) Список курсів, які певний викладач читає певному студенту (параметри: id студента, id викладача)')
        print(' 11) Середній бал, який певний викладач ставить певному студенту (параметри: id студента, id викладача)')
        print(' 12) Оцінки студентів у певній групі з певного предмету на останньому занятті (параметри: id групи, id предмета)')
        print('help - Команди')
        print(' exit - Вихід')