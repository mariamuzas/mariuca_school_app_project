from flask import Blueprint, Flask, redirect, render_template, request

from models.course import Course
import repositories.course_repository as course_repository

course_blueprint = Blueprint("course", __name__)

