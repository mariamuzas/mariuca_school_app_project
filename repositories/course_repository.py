from db.run_sql import run_sql
from models.course import Course
from models.student import Student

import repositories.student_repository as student_repository

def save(course):
    sql = "INSERT INTO courses ( title, description, date, duration, max_num_students, teacher_name) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [ course.title, course.description, course.date, course.duration, course.max_num_students, course.teacher_name]
    results = run_sql( sql, values )
    course.id = results[0]['id']
    return course


def select_all():
    courses = []

    sql = "SELECT * FROM courses"
    results = run_sql(sql)

    for row in results:
        course = Course(row['title'], row['description'], row['date'], row['duration'], row['max_num_students'], row['teacher_name'], row['id'])
        courses.append(course)
    return courses


def select(id):
    course = None 
    sql = "SELECT * FROM courses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        course = Course(result['title'], result['description'], result['date'], result['duration'], result['max_num_students'], result['teacher_name'], result['id'])
    return course

def delete(id):
    sql = "DELETE FROM courses WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM courses"
    run_sql(sql)


def update(course):
    sql = "UPDATE courses SET (title, description, date, duration, max_num_students, teacher_name) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [course.title, course.description, course.date, course.duration, course.max_num_students, course.teacher_name, course.id]
    run_sql(sql, values)


# def students(course):
#     students = []

#     sql = "SELECT * FROM students WHERE course_id = %s"
#     values = [course.id]
#     results = run_sql(sql, values)

#     for row in results: 
#         student = Student(row['name'], row['dob'], row['experience'], row['course_id'], row['id'])
#         students.append(student)
#     return students
