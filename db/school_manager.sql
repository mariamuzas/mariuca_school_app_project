DROP TABLE registrations;
DROP TABLE students;
DROP TABLE courses;

CREATE TABLE courses (
    id SERIAL PRIMARY KEY, 
    title VARCHAR(255),
    description VARCHAR(400),
    date VARCHAR(255),
    duration INT,
    max_num_students INT,
    teacher_name VARCHAR(255)
);

CREATE TABLE students(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE,
    experience VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255), 
    membership BOOLEAN
);

CREATE TABLE registrations(
    id SERIAL PRIMARY KEY, 
    course_id INT REFERENCES courses(id) ON DELETE CASCADE,
    student_id INT REFERENCES students(id) ON DELETE CASCADE
)
