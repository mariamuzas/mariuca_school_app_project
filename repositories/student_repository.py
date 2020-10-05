from db.run_sql import run_sql
from models.student import Student
from models.course import Course
import repositories.course_repository as course_repository

def save(student):
    sql = "INSERT INTO students(name, dob, experience, course_id ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [ student.name, student.dob, student.experience, student.course.id ]
    #  I have an error here, not sure how to fix
    results = run_sql( sql, values )
    student.id = results[0]['id']
    return student


def select_all():
    students = []

    sql = "SELECT * FROM students"
    results = run_sql(sql)

    for row in results:
        course_id = course_repository.select(row['course_id'])
        student = Student(row['name'], row['dob'], row['experience'], course_id, row['id'])
        students.append(student)
    return students


def select(id):
    student = None 
    sql = "SELECT * FROM students WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        course_id = course_repository.select(result['course_id'])
        student = Student(result['name'], result['dob'], result['experience'], course_id, result['id'])
    return student


def delete(id):
    sql = "DELETE FROM students WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# not sure if it is working 
def update(student):
    sql = "UPDATE students SET (name, dob, experience, course_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [student.name, student.dob, student.experience, student.course.id, student.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM students"
    run_sql(sql)

