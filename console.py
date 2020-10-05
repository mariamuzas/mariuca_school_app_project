import pdb
from models.student import Student
from models.course import Course
from models.registration import Registration

import repositories.student_repository as student_repository
import repositories.course_repository as course_repository
import repositories.registration_repository as registration_repository

student_repository.delete_all()
course_repository.delete_all()
registration_repository.delete_all()

course_1 = Course('Introduction to Bakery', 'Learn how to bake from scratch', 'Thursdays at 16pm', 2, 15, "Maria Antuna")
course_repository.save(course_1)

course_2 = Course('All I want for Christmas is food', 'Christmas Dinner Recipes', 'Saturdays at 10pm', 2, 10,'Maria Antuna')
course_repository.save(course_2)

course_3 = Course("Salads aren't boring", 'Vegetarian recipes that you never thought about', 'Tuesdays at 17pm', 1, 15, 'Berasategui')
course_repository.save(course_3)

student_1 = Student('Valerie Liberty', '10/04/1980', 'Intermediate', course_3)
student_repository.save(student_1)

student_2 = Student('Marco Botton', '07/07/1977', 'Beginner', course_2)
student_repository.save(student_2)

student_3 = Student('Alex Mateo', '12/09/1950', 'Advance', course_1)
student_repository.save(student_3)

registration_1 = Registration(course_1, student_1)
registration_repository.save(registration_1)

registration_2 = Registration(course_2, student_2)
registration_repository.save(registration_2)

registration_3 = Registration(course_3, student_3)
registration_repository.save(registration_3)

pdb.set_trace()