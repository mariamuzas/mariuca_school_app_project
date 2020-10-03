from db.run_sql import run_sql
from models.student import Student

def save(student):
    sql = "INSERT INTO students( name, dob, experience, course_id ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [ student.name, student.dob, student.experience, student.course_id]
    results = run_sql( sql, values )
    student.id = results[0]['id']
    return student
