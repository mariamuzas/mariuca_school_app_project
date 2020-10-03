from flask import Blueprint, Flask, redirect, render_template, request

from models.course import Course
import repositories.course_repository as course_repository

courses_blueprint = Blueprint("courses", __name__)

@courses_blueprint.route("/courses")
def courses():
    courses = course_repository.select_all()
    return render_template ("courses/index.html", courses = courses)