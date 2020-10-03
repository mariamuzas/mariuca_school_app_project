import pdb
from models.student import Student
from models.course import Course

import repositories.student_repository as student_repository
import repositories.course_repository as course_repository

student_repository.delete_all()
# course_repository.delete_all()
# they are triggering an index error, not sure why.

course_1 = Course('Introduction to Bakery', 'Learn how to bake from scratch', 'Thursdays at 16pm', 2, 15)
course_repository.save(course_1)

course_2 = Course('All I want for Christmas is food', 'Christmas Dinner Recipes', 'Saturdays at 10pm', 2, 10)
course_repository.save(course_2)

course_3 = Course("Salads aren't boring", 'Vegetarian recipes that you never thought about', 'Tuesdays at 17pm', 1, 15)
course_repository.save(course_3)

student1 = Student('Valerie Liberty', '43', 'Intermediate', 3)
student_repository.save(student1)

student1 = Student('Marco Botton', '28', 'Beginner', 1)
student_repository.save(student1)

student1 = Student('Alex Mateo', '35', 'Advance', 1)
student_repository.save(student1)



pdb.set_trace()