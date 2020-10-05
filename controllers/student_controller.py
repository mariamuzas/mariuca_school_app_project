from flask import Blueprint, Flask, redirect, render_template, request

from models.student import Student

import repositories.student_repository as student_repository
import repositories.course_repository as course_repository

student_blueprint = Blueprint("students", __name__)

@student_blueprint.route("/students")
def list_students():
    students = student_repository.select_all()
    return render_template ("students/index.html", students = students)

@student_blueprint.route("/students/new")
def new_student():
    courses = course_repository.select_all()
    return render_template("students/new.html", courses= courses)

@student_blueprint.route("/students", methods=["POST"])
def create_student():
    name = request.form["name"]
    dob = request.form["dob"]
    experience = request.form["experience"]
    course_id = request.form["course_id"]

    course_id = course_repository.select(course_id)

    student = Student(name, dob, experience, course_id)

    student_repository.save(student)
    return redirect("/students")

@student_blueprint.route("/students/<id>")
def show(id):
    student = student_repository.select(id)
    return render_template("students/show.html", student=student)

@student_blueprint.route("/students/<id>/delete", methods=["POST"])
def delete_student(id):
    student_repository.delete(id)
    return redirect("/students")

# @courses_blueprint.route("/courses/<id>/edit")
# def edit_course(id):
#     course = course_repository.select(id)
#     student = course_repository.students(course)
#     return render_template('courses/edit.html', course=course)

# @courses_blueprint.route("/courses/<id>", methods=["POST"])
# def update_course(id):
#     title = request.form["title"]
#     description = request.form ["description"]
#     date = request.form["date"]
#     duration = request.form["duration"]
#     max_num_students = request.form["max_num_students"]

#     course_to_update = Course(title, description, date, duration, max_num_students, id)

#     course_repository.update(course_to_update)
#     return redirect("/courses/<id>")

