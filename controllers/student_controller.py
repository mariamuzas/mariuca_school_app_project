from flask import Blueprint, Flask, redirect, render_template, request

from models.student import Student
import repositories.student_repository as student_repository

student_blueprint = Blueprint("student", __name__)

@student_blueprint.route("/list_students")
def list_students():
    students = student_repository.select_all()
    return render_template ("students/index.html", students = students)

