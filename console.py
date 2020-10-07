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

course_1 = Course('Bake It Till You Make It', "Nothing has family members running into the kitchen like the smell of something baking in the oven! This course will teach you all you need to know to make that perfect sharing food. From muffins to an Apple sponge you'll learn various techniques and methods you can apply to every baking endeavour you can imagine.", 'Thursdays at 16:00', 2, 15, "Maria Antuna")
course_repository.save(course_1)

course_2 = Course("All I Want For Christmas Is Food", "This stress-busting course will give you an array of options for the festive period and make sure you're ready to go when that time of year comes around. No need to panic anymore but be prepared, they'll have you making Christmas dinner every year for the rest of your life after this course!", "Saturdays at 10:00", 2, 10,"Maria Antuna")
course_repository.save(course_2)

course_3 = Course("The Cherry On Top", "Sure most meals don't end in dessert but when they do, they're always better. Learn to put the finishing touches on the perfect meal with our crash course in the most desired course of them all. Impressing a loved one, a special Birthday surprise for the kids or just making good old fashioned comfort food on a Tuesday  we've got you covered with our dessert masterclass. ", 'Tuesdays at 17:00', 1, 15, 'Martin Berasategui')
course_repository.save(course_3)

course_4 = Course("Salads Aren’t Boring", "As the world shifts to a more eco-friendly diet we want to remind you that eating good never felt so great. If you're wanting to improve your repertoire of vegetarian dishes, look no further than this course. From Compote to Gazpacho, don't ever let them tell you that being a vegetarian is boring!", 'Mondays at 17:00', 1, 15, 'Richard Wilson')
course_repository.save(course_4)

course_5 = Course("The New Delicacy", "The time for cheap standard meat dishes is over, now this delicacy needs to be savoured like the treat it is. We'll teach you how to wow your friends and family with these delightful yet simple dishes and not only that, we'll show you how to source, season and sample meats to ensure that you're doing your bit to keep our planet healthy!", 'Saturdays at 10:00', 1, 15, 'Richard Wilson')
course_repository.save(course_5)

course_6 = Course("Under The Sea!", "Hidden in rivers and under the sea lie some of the tastiest treats you could ever find. For a long time eating seafood has meant a prawn cocktail or fish supper but those days are gone with our amazing seafood course that'll show you exactly what Sebastien from Little Mermaid really was talking about, 'Life under the sea is better than anything they got up there!'", 'Fridays at 15:00', 1, 15, 'Martin Berasategui')
course_repository.save(course_6)

student_1 = Student('Valerie Liberty', '10/04/1980', 'Intermediate', "vliberty@gmail.com", '7852341700', True)
student_repository.save(student_1)

student_2 = Student('Marco Botton', '07/07/1977', 'Beginner', "bottonmarco@gmail.com", '7284932045', False)
student_repository.save(student_2)

student_3 = Student('Alex Mateo', '12/09/1950', 'Advanced', "mate0300@gmail.com",'7430328501', True )
student_repository.save(student_3)

student_4 = Student('Warren Peace', '3/07/1993', 'Advanced', "wpeace01@gmail.com",'7430334501', True )
student_repository.save(student_4)

student_5 = Student('Barbara Mendez','3/4/1990', 'Beginner', "barb1990@gmail.com", '7284932935', False)
student_repository.save(student_5)

student_6 = Student('James McFadden', '12/01/1989', 'Intermediate', "james@gmail.com", '7128432935', True)
student_repository.save(student_6)

student_7 = Student('Sonny Day', '12/04/1979', 'Intermediate', "sonnyday@gmail.com", '7128432845', False)
student_repository.save(student_7)

student_8 = Student('Nora Jones', "1/04/1993", 'Beginner', "morazoaz1993@gmail", '675822933', False)
student_repository.save(student_8)

registration_1 = Registration(course_1, student_1)
registration_repository.save(registration_1)

registration_2 = Registration(course_2, student_2)
registration_repository.save(registration_2)

registration_3 = Registration(course_3, student_3)
registration_repository.save(registration_3)

registration_4 = Registration(course_1, student_4)
registration_repository.save(registration_4)

registration_5 = Registration(course_1, student_3)
registration_repository.save(registration_5)

registration_6 = Registration(course_1, student_6)
registration_repository.save(registration_6)

registration_7 = Registration(course_2, student_6)
registration_repository.save(registration_7)

registration_8 = Registration(course_2, student_3)
registration_repository.save(registration_8)

registration_9 = Registration(course_2, student_1)
registration_repository.save(registration_9)


pdb.set_trace()