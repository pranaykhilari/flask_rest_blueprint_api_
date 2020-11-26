from flask import Blueprint
from flask_restful import Api

from .resource import Teacher

teacher_blueprint = Blueprint('teacher', __name__)
teacher_api = Api(teacher_blueprint)

routes = [
    '/create',
    '/get',
    '/get/<int:id>',
    '/update/<int:id>',
    '/delete/<int:id>'
]

teacher_api.add_resource(Teacher, *routes)
