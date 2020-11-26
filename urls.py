from student import student_blueprint
from teacher import teacher_blueprint


def url(app):
    app.register_blueprint(student_blueprint, url_prefix='/student')
    app.register_blueprint(teacher_blueprint, url_prefix='/teacher')
    return app
