import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    major TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    instructor TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students_courses (
    students_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY (students_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id),
    PRIMARY KEY (students_id, course_id)
)
""")

def create_student(name, age, major):
    cursor.execute("""
    INSERT INTO students (name, age, major)
    VALUES(?, ?, ?)
    """, (name, age, major))
    conn.commit()

def create_course(name, instructor):
    cursor.execute("""
    INSERT INTO courses (name, instructor)
    VALUES (?, ?)
    """, (name, instructor))
    conn.commit()

def select_all_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def select_all_courses():
    cursor.execute("SELECT * FROM courses")
    return cursor.fetchall()

def create_student_course(student_id, course_id):
    cursor.execute("""
    INSERT INTO students_courses (students_id, course_id)
    VALUES (?, ?)
    """, (student_id, course_id))
    conn.commit()

def select_students_by_course(course_id):
    cursor.execute("""
    SELECT students.name FROM students
    JOIN students_courses ON students.id = students_courses.students_id
    WHERE students_courses.course_id = ?
    """, (course_id,))
    return cursor.fetchall()
