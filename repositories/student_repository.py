from db.run_sql import run_sql
from models.student import Student
from models.course import Course
import repositories.course_repository as course_repository

def save(student):
    sql = "INSERT INTO students(name, dob, experience, email, phone, membership) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [ student.name, student.dob, student.experience, student.email, student.phone, student.membership ]
    results = run_sql( sql, values )
    student.id = results[0]['id']
    return student


def select_all():
    students = []

    sql = "SELECT * FROM students"
    results = run_sql(sql)

    for row in results:
        student = Student(row['name'], row['dob'], row['experience'], row['email'], row['phone'], row['membership'], row['id'] )
        students.append(student)
    return students


def select(id):
    student = None 
    sql = "SELECT * FROM students WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        student = Student(result['name'], result['dob'], result['experience'], result['email'], result['phone'], result['membership'], result['id'])
    return student


def delete(id):
    sql = "DELETE FROM students WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(student):
    sql = "UPDATE students SET (name, dob, experience, email, phone, membership) = (email, phone, membership, email, phone, membership) WHERE id = %s"
    values = [student.name, student.dob, student.experience, student.email, student.phone, student.membership, student.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM students"
    run_sql(sql)

