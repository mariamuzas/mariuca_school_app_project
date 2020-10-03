DROP TABLE bookings;
DROP TABLE students;
DROP TABLE courses;


CREATE TABLE courses(
    id SERIAL PRIMARY KEY, 
    title VARCHAR(255),
    description VARCHAR(255),
    date VARCHAR(255),
    duration INT,
    num_students INT
);

CREATE TABLE students(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    experience VARCHAR(255),
    course_id INT REFERENCES course(id)
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    course_id INT REFERENCES course(id),
    student_id INT REFERENCES student(id)
);
