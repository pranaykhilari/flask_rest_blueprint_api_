from flask import Blueprint
from flask_restful import Api

from .resource import Student

student_blueprint = Blueprint('student', __name__)
student_api = Api(student_blueprint)

routes = [
    '/create',
    '/get',
    '/get/<string:email>',
    '/update/<string:email>',
    '/delete/<string:email>'
]

student_api.add_resource(Student, *routes)




