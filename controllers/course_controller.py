from flask import Blueprint, Flask, redirect, render_template, request

from models.course import Course
import repositories.course_repository as course_repository

courses_blueprint = Blueprint("courses", __name__)

@courses_blueprint.route("/courses")
def list_courses():
    courses = course_repository.select_all()
    return render_template ("courses/index.html", courses = courses)

@courses_blueprint.route("/courses/new")
def new_course():
    return render_template("courses/new.html")

@courses_blueprint.route("/courses", methods =["POST"])
def create_course():
    title = request.form["title"]
    description = request.form ["description"]
    date = request.form["date"]
    duration = request.form["duration"]
    max_num_students = request.form["max_num_students"]

    course = Course(title, description, date, duration, max_num_students)

    course_repository.save(course)

    return redirect("/courses")

@courses_blueprint.route("/courses/<id>")
def show(id):
    course = course_repository.select(id)
    students = course_repository.students(course)
    return render_template("courses/show.html", course=course, students=students)

# @update and edit don't work! : list index error

@courses_blueprint.route("/courses/<id>/edit")
def edit_course(id):
    course = course_repository.select(id)
    student = course_repository.students(course)
    return render_template('courses/edit.html', course=course)

@courses_blueprint.route("/courses/<id>", methods=["POST"])
def update_course(id):
    title = request.form["title"]
    description = request.form ["description"]
    date = request.form["date"]
    duration = request.form["duration"]
    max_num_students = request.form["max_num_students"]

    course_to_update = Course(title, description, date, duration, max_num_students, id)

    course_repository.update(course_to_update)
    return redirect("/courses/<id>")

@courses_blueprint.route("/courses/<id>/delete", methods=["POST"])
def delete_course(id):
    course_repository.delete(id)
    return redirect("/courses")