class Course:
    def __init__(self, title, description, date, duration, max_num_students, teacher_name = None, id = None):
        self.title = title
        self.description = description
        self.date = date
        self.duration = duration
        self.max_num_students = max_num_students
        self.teacher_name = teacher_name
        self.id = id