from flask import Blueprint, Flask, redirect, render_template, request

from models.student import Student
from models.registration import Registration

import repositories.student_repository as student_repository
import repositories.course_repository as course_repository
import repositories.registration_repository as registration_repository

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

    course = course_repository.select(course_id)
    new_student = Student(name, dob, experience)
    new_registration = Registration(course, new_student)

    student_repository.save(new_student)
    registration_repository.save(new_registration)
    return redirect(f"/students/{new_student.id}")

@student_blueprint.route("/students/<id>")
def show(id):
    student = student_repository.select(id)
    courses = registration_repository.select_courses(id)
    return render_template("students/show.html", student=student, courses= courses)

@student_blueprint.route("/students/<id>/delete", methods=["POST"])
def delete_student(id):
    student_repository.delete(id)
    return redirect("/students")

@student_blueprint.route("/students/<id>/edit")
def edit_student(id):
    courses = course_repository.select_all()
    student = student_repository.select(id)
    return render_template('students/edit.html', student= student, courses=courses)

@student_blueprint.route("/students/<id>", methods=["POST"])
def update_student(id):
    name = request.form["name"]
    dob = request.form["dob"]
    experience = request.form["experience"]
    course_id = request.form["course_id"]

    course = course_repository.select(course_id)
    student_to_update = Student(name, dob, experience, id)
    student_repository.update(student_to_update)
    return redirect(f"/students/{student_to_update.id}")
