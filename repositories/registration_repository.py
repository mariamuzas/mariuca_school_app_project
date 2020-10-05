from db.run_sql import run_sql

from models.registration import Registration
from models.student import Student
from models.course import Course

import repositories.student_repository as student_repository
import repositories.course_repository as course_repository


def save(registration):
    sql = "INSERT INTO registrations (course_id, student_id) VALUES (%s, %s) returning id"
    values = [registration.course.id, registration.student.id]
    results = run_sql(sql, values)
    registration.id = results[0]['id']
    return registration


def select_all():
    registrations = []

    sql = "SELECT * FROM registrations"
    results = run_sql(sql)

    for row in results:
        course = course_repository.select(row['course_id'])
        student = student_repository.select(row['student_id'])
        registration = Registration(course, student, row['id'])
        registrations.append(registration)
    return registrations


def delete_all():
    sql = "DELETE FROM registrations"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM registrations WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# def course(registration):
#     sql = "SELECT * FROM registrations WHERE id = %s"
#     values = [registration.course.id]
#     results = run_sql(sql, values)[0]
#     course = Course(results['title'], results['description'], results['date'], results['duration'], results['max_num_students'], results['teacher_name'], results['id'])
#     return course

# def student(registration):
#     sql = "SELECT * FROM registrations WHERE id = %s"
#     values = [registration.student.id]
#     results = run_sql(sql, values)[0]

#     student = Student(results['name'], results['dob'], results['experience'], results['course_id'], results['id']) 
    
#     return student
