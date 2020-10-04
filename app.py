from flask import Flask, render_template

from controllers.course_controller import courses_blueprint
from controllers.student_controller import student_blueprint

app = Flask(__name__)

app.register_blueprint(courses_blueprint)
app.register_blueprint(student_blueprint)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()