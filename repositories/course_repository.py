from db.run_sql import run_sql
from models.course import Course


def save(course):
    sql = "INSERT INTO courses ( title, description, date, duration, max_num_students ) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [ course.title, course.description, course.date, course.duration, course.max_num_students ]
    results = run_sql( sql, values )
    course.id = results[0]['id']
    return course

def select_all():
    courses = []

    sql = "SELECT * FROM courses"
    results = run_sql(sql)

    for row in results:
        course = Course(row['title'], row['description'], row['date'], row['duration'], row['max_num_student'])
        courses.append(course)
    return course
