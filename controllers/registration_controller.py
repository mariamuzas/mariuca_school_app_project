from flask import Blueprint, Flask, redirect, render_template, request

from models.student import Student
from models.course import Course
from models.registration import Registration

import repositories.student_repository as student_repository
import repositories.course_repository as course_repository
import repositories.registration_repository as registration_repository

registration_blueprint = Blueprint('registration', __name__)

@registration_blueprint.route("/registrations")
def list_registrations():
    registrations = registration_repository.select_all()
    return render_template('registrations/index.html', registrations = registrations)


@registration_blueprint.route("/registrations/<id>/delete", methods= ["POST"])
def delete_registration(id):
    registration_repository.delete(id)
    return redirect("/registrations")


@registration_blueprint.route("/registrations/<id>/edit")
def edit_registration(id):
    students = student_repository.select_all()
    courses = course_repository.select_all()
    registration = registration_repository.select(id)
    return render_template('registrations/edit.html', registration= registration, students=students, courses=courses )


@registration_blueprint.route("/registrations/<id>", methods=["POST"])
def update_registration(id):
    course_id = request.form["course_id"]
    student_id = request.form["student_id"]

    course = course_repository.select(course_id)
    student= student_repository.select(student_id)

    registration_to_update = Registration(course, student, id)
    registration_repository.update(registration_to_update)
    return redirect("/registrations")
