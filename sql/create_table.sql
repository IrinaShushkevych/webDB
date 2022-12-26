-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(150) NOT NULL,
    id_group INTEGER,
    FOREIGN KEY (id_group) REFERENCES groups (id)
);

--Table: group
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(20) NOT NULL
);

--Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name VARCHAR(150) NOT NULL
);

--Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(150) NOT NULL,
    id_teacher INTEGER,
    FOREIGN KEY (id_teacher) REFERENCES teachers (id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

--Table: gradebook
DROP TABLE IF EXISTS gradebook;
CREATE TABLE gradebook(
    id_student INTEGER,
    id_subject INTEGER,
    grade INTEGER NOT NULL DEFAULT 0,
    createdAt DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY (id_student, id_subject, createdAt),
    FOREIGN KEY (id_student) REFERENCES students (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (id_subject) REFERENCES subjects (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
