from flask import Blueprint, Flask, redirect, render_template, request

from models.course import Course
import repositories.course_repository as course_repository

courses_blueprint = Blueprint("courses", __name__)

@courses_blueprint.route("/courses")
def courses():
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

